import logging
from django.shortcuts import redirect, render
from .forms import TicketForm
from .models import Ticket

logger = logging.getLogger(__name__)


def ticket_list_and_create(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            logger.info("Өтінім сақталды, ID=%s", ticket.pk)
            return redirect("ticket_list")
        else:
            logger.warning("Өтінім формасы тексеруден өтпеді")
    else:
        form = TicketForm()

    tickets = Ticket.objects.order_by("-created_at")
    return render(
        request,
        "tickets/index.html",
        {"form": form, "tickets": tickets},
    )