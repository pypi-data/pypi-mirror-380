import { createElement } from "./createElement.js";
import { state } from "../state.js";
import {getTicketMessages, setTicketViewed} from "../scripts/apiController.js";
import {
    btnSetMyTicketsElement,
    btnSetUnassignedTicketsElement,
    managerIdElement,
    ticketAssignElement,
    ticketTitleElement,
} from "../const/ELEMENTS.js";


async function handleClick(ticket, ticketEl, indicatorEl) {
    if (ticket.viewed || ticketEl.dataset.loading === "1") {
        state.setCurrentChatId(ticket.id);
        getTicketMessages(ticket.id);
        ticketTitleElement.textContent = ticket.title;
        ticketAssignElement.disabled = Boolean(ticket.support_manager);
        ticketAssignElement.value = ticketAssignElement.disabled ? "В работе" : "Принять в работу";
        ticketAssignElement.disabled
            ? ticketAssignElement.classList.add("!bg-gray-600")
            : ticketAssignElement.classList.remove("!bg-gray-600");
        return;
    }

    ticketEl.dataset.loading = "1";
    try {
        await setTicketViewed(ticket.id);
        ticket.viewed = true;
        indicatorEl?.remove();
    } catch (e) {
        console.error(e);
    } finally {
        delete ticketEl.dataset.loading;
    }

    state.setCurrentChatId(ticket.id);
    getTicketMessages(ticket.id);
    ticketTitleElement.textContent = ticket.title;
    ticketAssignElement.disabled = Boolean(ticket.support_manager);
    ticketAssignElement.value = ticketAssignElement.disabled ? "В работе" : "Принять в работу";
    ticketAssignElement.disabled
        ? ticketAssignElement.classList.add("!bg-gray-600")
        : ticketAssignElement.classList.remove("!bg-gray-600");
}

export function addTicketToList(ticketData) {
    if (
        ticketData.support_manager &&
        ticketData.support_manager?.id != managerIdElement.textContent
    )
        return;
    if (!ticketData.support_manager && !btnSetUnassignedTicketsElement.disabled) return;
    if (ticketData.support_manager && !btnSetMyTicketsElement.disabled) return;

    const ticketList = document.querySelector(".ticket-list");

    const indicator = ticketData.viewed
        ? null
        : createElement("span", {
            classes: [
                "ml-auto",
                "w-3",
                "h-3",
                "rounded-full",
                "bg-red-500",
                "inline-block",
                "self-center",
            ],
        });
    const ticketElement = createElement("div", {
        classes: [
            "w-full",
            "h-fit",
            "rounded",
            "cursor-pointer",
            "bg-[#111827]",
            "p-4",
            "shadow-md",
            "text-white",
        ],
        attributes: { "data-ticket-id": ticketData.id },
        children: [
            createElement("h1", {
                textContent: ticketData.title,
                classes: ["text-lg", "font-bold"],
            }),
            createElement("h6", {
                textContent: `Создан: ${new Date(ticketData.created_at).toLocaleString()}`,
            }),
            createElement("h6", {
                textContent: `Менеджер: ${ticketData.support_manager?.first_name ?? "Не назначен"}`,
            }),
            indicator,
        ],
    });
    // const ticketId = ticketElement.getAttribute('data-ticket-id');
    ticketElement.addEventListener("click", () => handleClick(ticketData, ticketElement, indicator));
    ticketList.prepend(ticketElement);
}
