from django.utils.translation import gettext as _

from pretalx.common.phrases import Phrases


class OrgaPhrases(Phrases, app="orga"):

    logged_in = [
        _("Hi, nice to see you!"),
        _("Welcome!"),
        _("I hope you are having a good day :)"),
        _("Remember: organising events is lots of work, but it pays off."),
        _(
            "If you are waiting for feedback from your speakers, try sending a mail to a subset of them."
        ),
        _(
            "Remember to provide your speakers with all information they need ahead of time."
        ),
        _(
            "Even the busiest event organisers should make time to see at least one session ;)"
        ),
    ]
    schedule_example_version = [
        "v1",
        "v2",
        "v4.0",
        "v0.1",
        "♥",
    ]
    example_answer = [
        _("Pudding"),
        _("Panna cotta"),
        _("Chocolate chip cookies"),
    ]
    example_review = [
        _("I think this session is well-suited to this conference, because ..."),
        _("I think this session might fit the conference better, if ..."),
        _("I think this session sounds like a perfect fit for Day 2, since ..."),
        _("I think this session might be improved by adding ..."),
        _("I have heard a similar session by this speaker, and I think ..."),
        _("In my opinion, this session will appeal to ..."),
        _("While I think the session is a great fit, it might be improved by ..."),
    ]
