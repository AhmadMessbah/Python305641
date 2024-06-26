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
    def edit(group, title, text, sender, date_time):
        try:
            ticket = Ticket(group, title, text, sender, date_time)
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
    @staticmethod
    def find_by_group(group):
        try:
            ticket = TicketService.find_by_group(group)
            Logger.info(f"Ticket FindByGroup({group})")
            return True, ticket
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_title(title):
        try:
            ticket = TicketService.find_by_title(title)
            Logger.info(f"Ticket FindByTitle({title})")
            return True, ticket
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_text_content(text_content):
        try:
            ticket = TicketService.find_by_text_content(text_content)
            Logger.info(f"Ticket FindByTextContent({text_content})")
            return True, ticket
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def date_range(start_date, end_date):
        try:
            ticket = TicketService.date_range(start_date, end_date)
            Logger.info(f"Ticket FindByTextContent({start_date}-{end_date})")
            return True, ticket
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"