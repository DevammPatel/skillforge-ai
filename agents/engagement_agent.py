class EngagementAgent:

    def generate(
        self,
        meeting_hours,
        focus_hours,
        risk
    ):

        if meeting_hours > 20:
            reminder_window = "morning focus block"
            cadence = "3 short reminders per week"

        elif focus_hours >= 18:
            reminder_window = "afternoon deep-work window"
            cadence = "2 progress nudges per week"

        else:
            reminder_window = "first available focus window"
            cadence = "daily lightweight check-ins"

        escalation = (
            "Notify the manager if two weekly checkpoints are missed."
            if risk == "High"
            else "Keep reminders learner-owned unless readiness drops."
        )

        return f"""
## Engagement Plan

**Recommended reminder cadence:** {cadence}

**Best reminder window:** {reminder_window}

**Work-context rationale:** The learner has **{meeting_hours} meeting hours** and **{focus_hours} focus hours**, so reminders should avoid peak meeting load and reinforce protected learning time.

**Escalation rule:** {escalation}

**Privacy note:** Uses synthetic workload signals only and avoids exposing personal communication data.
"""
