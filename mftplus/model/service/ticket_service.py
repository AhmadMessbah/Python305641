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


    # todo : find by group, title, text_contain, sender, date_time_range