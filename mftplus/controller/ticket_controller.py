from mftplus.model.entity.ticket import Ticket
from mftplus.model.service.ticket_service import TicketService
from mftplus.model.tools.logger import Logger


class TicketController:
    @staticmethod
    def save(group, title, text, sender, date_time):
        try:
            ticket = Ticket(group, title, text, sender, date_time)
            TicketService.save(ticket)
            Logger.info(f"Ticket Saved - {ticket}")
            return True, ticket
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def edit(id, name, family):
        try:
            ticket = Ticket("ahmad", "messbah")
            ticket.id = id
            TicketService.edit(ticket)
            Logger.info(f"Ticket Edited - {ticket}")
            return True, ticket
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def remove(id):
        try:
            ticket = TicketService.remove(id)
            Logger.info(f"Ticket Removed - {ticket}")
            return True, ticket
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def findAll():
        try:
            ticket_list = TicketService.find_all()
            Logger.info(f"Ticket FindAll()")
            return True, ticket_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_id(id):
        try:
            ticket = TicketService.find_by_id(id)
            Logger.info(f"Ticket FindById({id})")
            return True, ticket
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"
