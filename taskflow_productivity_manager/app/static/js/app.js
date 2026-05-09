/*
Small usability enhancement.

The app works without JavaScript, but this prevents accidental task deletion.
*/

document.addEventListener("DOMContentLoaded", () => {
    const forms = document.querySelectorAll("form[data-confirm]");

    forms.forEach((form) => {
        form.addEventListener("submit", (event) => {
            const message = form.getAttribute("data-confirm");

            if (!confirm(message)) {
                event.preventDefault();
            }
        });
    });
});
