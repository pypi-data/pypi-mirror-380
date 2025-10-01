from dateutil.relativedelta import relativedelta
from edc_visit_schedule.constants import DAY1, MONTH1, MONTH3, MONTH6, WEEK2
from edc_visit_schedule.schedule import Schedule
from edc_visit_schedule.visit import Crf, CrfCollection, Visit
from edc_visit_schedule.visit_schedule import VisitSchedule

from ..dummy_panel import DummyPanel


def get_visit_schedule(cdef):
    app_label = "clinicedc_tests"

    class MockPanel(DummyPanel):
        """`requisition_model` is normally set when the lab profile
        is set up.
        """

        def __init__(self, name):
            super().__init__(
                requisition_model="clinicedc_tests.subjectrequisition", name=name
            )

    crfs_prn = CrfCollection(
        Crf(show_order=100, model=f"{app_label}.prnone"),
        Crf(show_order=200, model=f"{app_label}.prntwo"),
    )

    crfs_missed = CrfCollection(
        Crf(show_order=1, model="edc_visit_tracking.subjectvisitmissed", required=True),
    )

    crfs0 = CrfCollection(
        Crf(show_order=1, model=f"{app_label}.crftwo", required=False)
    )
    crfs1 = CrfCollection(Crf(show_order=1, model=f"{app_label}.crfone", required=True))
    crfs2 = CrfCollection(
        Crf(show_order=1, model=f"{app_label}.crfone", required=False)
    )
    crfs3 = CrfCollection(
        Crf(show_order=1, model=f"{app_label}.crfone", required=False)
    )
    crfs4 = CrfCollection(
        Crf(show_order=1, model=f"{app_label}.crfone", required=False)
    )

    visit0 = Visit(
        code=DAY1,
        title="Week 1",
        timepoint=0.0,
        rbase=relativedelta(days=0),
        rlower=relativedelta(days=0),
        rupper=relativedelta(days=6),
        crfs=crfs0,
        crfs_prn=crfs_prn,
        allow_unscheduled=True,
        facility_name="5-day-clinic",
    )

    visit1 = Visit(
        code=WEEK2,
        title="Week 2",
        timepoint=1.0,
        rbase=relativedelta(days=7),
        rlower=relativedelta(days=0),
        rupper=relativedelta(days=6),
        crfs=crfs1,
        crfs_prn=crfs_prn,
        crfs_missed=crfs_missed,
        facility_name="5-day-clinic",
    )

    visit2 = Visit(
        code=MONTH1,
        title="Month 1",
        timepoint=2.0,
        rbase=relativedelta(months=1),
        rlower=relativedelta(days=0),
        rupper=relativedelta(days=6),
        crfs=crfs2,
        crfs_prn=crfs_prn,
        facility_name="5-day-clinic",
    )

    visit3 = Visit(
        code=MONTH3,
        title="Month 3",
        timepoint=3.0,
        rbase=relativedelta(months=3),
        rlower=relativedelta(days=0),
        rupper=relativedelta(days=6),
        crfs=crfs3,
        crfs_prn=crfs_prn,
        facility_name="5-day-clinic",
    )

    visit4 = Visit(
        code=MONTH6,
        title="Month 6",
        timepoint=4.0,
        rbase=relativedelta(months=6),
        rlower=relativedelta(days=0),
        rupper=relativedelta(days=6),
        crfs=crfs4,
        crfs_prn=crfs_prn,
        facility_name="5-day-clinic",
    )

    schedule = Schedule(
        name="schedule",
        onschedule_model="edc_visit_schedule.onschedule",
        offschedule_model="clinicedc_tests.offschedule",
        consent_definitions=[cdef],
        appointment_model="edc_appointment.appointment",
    )

    schedule.add_visit(visit0)
    schedule.add_visit(visit1)
    schedule.add_visit(visit2)
    schedule.add_visit(visit3)
    schedule.add_visit(visit4)

    visit_schedule = VisitSchedule(
        name="visit_schedule",
        offstudy_model="edc_offstudy.subjectoffstudy",
        death_report_model="clinicedc_tests.deathreport",
    )

    visit_schedule.add_schedule(schedule)
    return visit_schedule
