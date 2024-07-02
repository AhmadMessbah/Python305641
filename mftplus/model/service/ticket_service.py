from mftplus.controller.exceptions.exeptions import TicketNotFoundError
from mftplus.model.da.da import DataAccess
from mftplus.model.entity.ticket import Ticket


class TicketService:
    @staticmethod
    def save(ticket):
        ticket_da = DataAccess(Ticket)
        ticket_da.save(ticket)
        return ticket

    @staticmethod
    def edit(ticket):
        ticket_da = DataAccess(Ticket)
        if ticket_da.find_by_id(ticket.id):
            ticket_da.edit(ticket)
            return ticket
        else:
            raise TicketNotFoundError()

    @staticmethod
    def remove(id):
        ticket_da = DataAccess(Ticket)
        if ticket_da.find_by_id(id):
            return ticket_da.remove(id)
        else:
            raise TicketNotFoundError()

    @staticmethod
    def find_all():
        ticket_da = DataAccess(Ticket)
        return ticket_da.find_all()

    @staticmethod
    def find_by_id(id):
        ticket_da = DataAccess(Ticket)
        return ticket_da.find_by_id(id)

    @staticmethod
    def find_by_group(group):
        ticket_da = DataAccess(Ticket)
        return ticket_da.find_by(Ticket._group == group)

    @staticmethod
    def find_by_title(title):
        ticket_da = DataAccess(Ticket)
        return ticket_da.find_by(Ticket._title == title)

    @staticmethod
    def find_by_text_content(text_content):
        ticket_da = DataAccess(Ticket)
        return ticket_da.check_word_in_text(text_content)

    @staticmethod
    def date_range(start_date, end_date):
        ticket_da = DataAccess(Ticket)
        return ticket_da.find_by_date_range(start_date, end_date)
