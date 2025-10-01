from __future__ import annotations

import os
import sys
from datetime import datetime
from importlib.resources import files
from typing import List
from uuid import uuid4
from zoneinfo import ZoneInfo

from dateutil.relativedelta import relativedelta
from multisite import SiteID

__all__ = ["DefaultTestSettings"]


class DisableMigrations(dict):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


def get_migrations_module():
    return DisableMigrations()


class DefaultTestSettings:
    """Return settings with reasonable defaults.

    Expects a project structure where the root is the repo
    and the application is a sub-folder of the repo. For example:

      edc-crf/edc_crf/
      edc-crf/edc_crf/tests/
      edc-crf/edc_crf/tests/holiday.csv
      edc-crf/edc_crf/tests/tests_settings.py
      edc-crf/edc_crf/tests/models.py
      edc-crf/edc_crf/tests/urls.py
      edc-crf/edc_crf/tests/etc/
      edc-crf/edc_crf/tests/tests/
      edc-crf/edc_crf/tests/tests/test_crfs.py

      this implies

      GIT_DIR = edc-crf/
      BASE_DIR = edc-crf/
      HOLIDAY_DIR = edc-crf/edc_crf/tests/
      ETC_DIR = edc-crf/edc_crf/tests/etc

    """

    def __init__(
        self,
        base_dir=None,
        app_name=None,
        calling_file=None,
        use_test_urls=None,
        add_dashboard_middleware=None,
        add_lab_dashboard_middleware=None,
        add_adverse_event_dashboard_middleware=None,
        add_multisite_middleware=None,
        template_dirs=None,
        selected_database: str = None,
        **kwargs,
    ):
        self.calling_file = os.path.basename(calling_file) if calling_file else None
        self.base_dir = base_dir or kwargs.get("BASE_DIR")
        self.app_name = app_name or kwargs.get("APP_NAME")
        self.selected_database = selected_database or "sqlite"
        self.installed_apps = kwargs.get("INSTALLED_APPS")

        self.settings = dict(
            APP_NAME=self.app_name,
            BASE_DIR=self.base_dir,
            INSTALLED_APPS=self.installed_apps,
            ETC_DIR=kwargs.get("ETC_DIR")
            or self.base_dir / self.app_name / "tests" / "etc",
            TEST_DIR=kwargs.get("TEST_DIR") or self.base_dir / self.app_name / "tests",
            HOLIDAY_FILE=(
                kwargs.get("HOLIDAY_FILE") or files("clinicedc_tests") / "holidays.csv"
            ),
        )

        self._update_defaults()
        # override / add from params
        self.settings.update(**kwargs)

        if template_dirs:
            self.settings["TEMPLATES"][0]["DIRS"] = template_dirs

        self.update_root_urlconf(use_test_urls)
        if not add_multisite_middleware:
            self.settings["MIDDLEWARE"].remove(
                "multisite.middleware.DynamicSiteMiddleware"
            )

        if add_dashboard_middleware:
            self.settings["MIDDLEWARE"].extend(
                [
                    "edc_protocol.middleware.ResearchProtocolConfigMiddleware",
                    "edc_dashboard.middleware.DashboardMiddleware",
                    "edc_subject_dashboard.middleware.DashboardMiddleware",
                    "edc_listboard.middleware.DashboardMiddleware",
                    "edc_review_dashboard.middleware.DashboardMiddleware",
                ]
            )

        if add_lab_dashboard_middleware:
            self.settings["MIDDLEWARE"].extend(
                ["edc_lab_dashboard.middleware.DashboardMiddleware"]
            )
        if add_adverse_event_dashboard_middleware:
            self.settings["MIDDLEWARE"].extend(
                ["edc_adverse_event.middleware.DashboardMiddleware"]
            )

        if "django_crypto_fields.apps.AppConfig" in self.installed_apps:
            self._manage_encryption_keys()
        self.check_travis()
        self.check_github_actions()

    def update_root_urlconf(self, use_test_urls=None):
        if "ROOT_URLCONF" not in self.settings:
            if use_test_urls:
                self.settings.update(ROOT_URLCONF=f"{self.app_name}.tests.urls")
            else:
                self.settings.update(ROOT_URLCONF=f"{self.app_name}.urls")

    @property
    def default_context_processors(self) -> List[str]:
        return [
            "django.contrib.auth.context_processors.auth",
            "django.contrib.messages.context_processors.messages",
            "django.template.context_processors.request",
        ]

    @property
    def edc_context_processors(self) -> List[str]:
        context_processors = []
        if [a for a in self.installed_apps if a.startswith("edc_model_admin")]:
            context_processors.append("edc_model_admin.context_processors.admin_theme")
        if [a for a in self.installed_apps if a.startswith("edc_constants")]:
            context_processors.append("edc_constants.context_processors.constants")
        if [a for a in self.installed_apps if a.startswith("edc_appointment")]:
            context_processors.append("edc_appointment.context_processors.constants")
        if [a for a in self.installed_apps if a.startswith("edc_visit_tracking")]:
            context_processors.append("edc_visit_tracking.context_processors.constants")
        return context_processors

    def _update_defaults(self):
        """Assumes BASE_DIR is project/src and tests of at project/tests."""

        utcnow = datetime.now().astimezone(ZoneInfo("UTC"))

        context_processors = self.default_context_processors
        context_processors.extend(self.edc_context_processors)
        if not self.selected_database or self.selected_database == "sqlite":
            databases = self.sqlite_databases_setting()
        elif self.selected_database == "mysql":
            databases = self.mysql_databases_setting()
        elif self.selected_database == "mysql_with_client":
            databases = self.mysql_databases_setting(client=True)
        self.settings.update(
            ALLOWED_HOSTS=["localhost"],
            STATIC_URL="/static/",
            DATABASES=databases,
            TEMPLATES=[
                {
                    "BACKEND": "django.template.backends.django.DjangoTemplates",
                    "APP_DIRS": True,
                    "OPTIONS": {"context_processors": context_processors},
                }
            ],
            MIDDLEWARE=[
                "django.middleware.security.SecurityMiddleware",
                "django.contrib.sessions.middleware.SessionMiddleware",
                "django.middleware.locale.LocaleMiddleware",
                "django.middleware.common.CommonMiddleware",
                "django.middleware.csrf.CsrfViewMiddleware",
                "django.contrib.auth.middleware.AuthenticationMiddleware",
                "django.contrib.messages.middleware.MessageMiddleware",
                "django.middleware.clickjacking.XFrameOptionsMiddleware",
                "multisite.middleware.DynamicSiteMiddleware",
                "django.contrib.sites.middleware.CurrentSiteMiddleware",
            ],
            LANGUAGE_CODE="en",
            TIME_ZONE="UTC",
            USE_I18N=True,
            USE_L10N=True,
            USE_TZ=True,
            DEFAULT_AUTO_FIELD="django.db.models.BigAutoField",
            GIT_DIR=self.base_dir,
            LIVE_SYSTEM=False,
            REVIEWER_SITE_ID=0,
            SITE_ID=SiteID(default=1) if SiteID else 1,
            SILENCED_SYSTEM_CHECKS=[
                "sites.E101"
            ],  # The SITE_ID setting must be an integer
            SECRET_KEY=uuid4().hex,
            INDEX_PAGE_LABEL="",
            DASHBOARD_URL_NAMES={},
            DASHBOARD_BASE_TEMPLATES={},
            EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
            EMAIL_CONTACTS={
                "data_request": "someone@example.com",
                "data_manager": "someone@example.com",
                "tmg": "someone@example.com",
            },
            EMAIL_ENABLED=False,
            INDEX_PAGE="http://localhost:8000",
            SENTRY_ENABLED=False,
            TWILIO_ENABLED=False,
            TWILIO_TEST_RECIPIENT="+15555555555",
            SUBJECT_SCREENING_MODEL="clinicedc_tests.subjectscreening",
            SUBJECT_CONSENT_MODEL="clinicedc_tests.subjectconsent",
            SUBJECT_VISIT_MODEL="edc_visit_tracking.subjectvisit",
            SUBJECT_VISIT_MISSED_MODEL="edc_visit_tracking.subjectvisitmissed",
            SUBJECT_REQUISITION_MODEL="clinicedc_tests.subjectrequisition",
            SUBJECT_REFUSAL_MODEL="edc_refusal.subjectrefusal",
            SUBJECT_APP_LABEL="clinicedc_tests",
            ADVERSE_EVENT_ADMIN_SITE="clinicedc_tests",
            ADVERSE_EVENT_APP_LABEL="clinicedc_tests",
            EDC_LTFU_MODEL_NAME="edc_ltfu.ltfu",
            DJANGO_COLLECT_OFFLINE_ENABLED=False,
            DJANGO_COLLECT_OFFLINE_FILES_REMOTE_HOST=None,
            DJANGO_COLLECT_OFFLINE_FILES_USB_VOLUME=None,
            DJANGO_COLLECT_OFFLINE_FILES_USER=None,
            DJANGO_COLLECT_OFFLINE_SERVER_IP=None,
            EDC_NAVBAR_DEFAULT="clinicedc_tests",
            EDC_PROTOCOL_PROJECT_NAME="CLINICEDC TEST PROJECT",
            EDC_PROTOCOL_STUDY_OPEN_DATETIME=(
                utcnow.replace(microsecond=0, second=0, minute=0, hour=0)
                - relativedelta(years=1)
            ),
            EDC_PROTOCOL_STUDY_CLOSE_DATETIME=(
                utcnow.replace(microsecond=999999, second=59, minute=59, hour=11)
                + relativedelta(years=1)
            ),
            EDC_PROTOCOL_NUMBER="101",
            EDC_FACILITY_USE_DEFAULTS=True,
            EDC_FACILITY_DEFAULT_FACILITY_NAME="7-day-clinic",
            LIST_MODEL_APP_LABEL="clinicedc_tests",
            EDC_RANDOMIZATION_LIST_PATH=self.base_dir.parent / "tests" / "etc",
            EDC_RANDOMIZATION_REGISTER_DEFAULT_RANDOMIZER=True,
            EDC_RANDOMIZATION_SKIP_VERIFY_CHECKS=True,
            EDC_DATA_MANAGER_POPULATE_DATA_DICTIONARY=False,
            EDC_VISIT_SCHEDULE_POPULATE_VISIT_SCHEDULE=True,
            EDC_SITES_MODULE_NAME=None,
            MULTISITE_REGISTER_POST_MIGRATE_SYNC_ALIAS=False,
            DATA_DICTIONARY_APP_LABELS=[],
            DEFAULT_FILE_STORAGE="inmemorystorage.InMemoryStorage",
            MIGRATION_MODULES=get_migrations_module(),
            PASSWORD_HASHERS=("django.contrib.auth.hashers.MD5PasswordHasher",),
        )

    def _manage_encryption_keys(self):
        # update settings if running runtests directly from the command line
        if self.calling_file and self.calling_file == sys.argv[0]:
            key_path = self.settings.get("ETC_DIR")
            if not os.path.exists(key_path):
                os.mkdir(key_path)
            auto_create_keys = True if len(os.listdir(key_path)) == 0 else False
            self.settings.update(
                DEBUG=False,
                DJANGO_CRYPTO_FIELDS_KEY_PATH=key_path,
                AUTO_CREATE_KEYS=auto_create_keys,
            )

    def check_github_actions(self):
        if os.environ.get("GITHUB_ACTIONS"):
            self.settings.update(DATABASES=self.mysql_databases_setting(client=True))

    def check_travis(self):
        if os.environ.get("TRAVIS"):
            self.settings.update(DATABASES=self.mysql_databases_setting())

    @staticmethod
    def mysql_databases_setting(client: bool | None = None) -> dict:
        databases = {
            "default": {
                "ENGINE": "django.db.backends.mysql",
                "NAME": "test_db",
                "USER": "root",
                "PASSWORD": "root",
                "HOST": "127.0.0.1",
                "PORT": 3306,
            }
        }
        if client:
            databases.update(
                {
                    "client": {
                        "ENGINE": "django.db.backends.mysql",
                        "NAME": "test_db2",
                        "USER": "root",
                        "PASSWORD": "root",
                        "HOST": "127.0.0.1",
                        "PORT": 3306,
                    }
                }
            )

        return databases

    def sqlite_databases_setting(self):
        return {
            # required for tests when acting as a server that deserializes
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": self.base_dir / "db.sqlite3",
            },
            "client": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": self.base_dir / "db.sqlite3",
            },
        }
