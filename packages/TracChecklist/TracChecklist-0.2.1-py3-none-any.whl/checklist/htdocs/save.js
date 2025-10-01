 /*
  Checklist Auto-Save Script - triggered when any step in a checklist
  is set or unset to call the database API and update the form state.
 */


// DEBOUNCE - delay (in milliseconds) to wait after user actions
const DEBOUNCE_DELAY = 800;
let debounceTimer;

// SEND - send a single form as multipart/form‑data
async function submitChecklistForm(formEl) {
  const formId   = formEl.id;

  // show save spinner bar
  document.querySelectorAll(".loader").forEach(x => x.style.visibility = "visible");

  // Build a FormData object that automatically includes *all* fields
  const payload = new FormData(formEl);

  // Perform update – because we are sending FormData we do NOT set
  // a Content‑Type header; the browser adds the correct multipart boundary.
  try {
    const response = await fetch(formEl.action, {
      method: 'POST',
      body: payload,
      credentials: 'same-origin'
    });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    } else {
      console.log(`Form "${formId}" saved:`, response.status);
    }

  } catch (err) {
    console.error(`Error submitting form "${formId}":`, err);
  }

  // hide loader bar
  document.querySelectorAll(".loader").forEach(x => x.style.visibility = "hidden");
  document.querySelectorAll(".saved").forEach(x => x.style.visibility = "visible");
  document.querySelectorAll(".source").forEach(x => x.style.background = "#cfffc1");

}

// EVENT BINDING – one listener per form, attached to its check‑boxes
document.querySelectorAll('form.checklist').forEach(form => {
  // Attach a single delegated listener to the form itself.
  // It will fire for any change event bubbling up from a checkbox.
  form.addEventListener('change', ev => {
    if (ev.target && ev.target.type === 'checkbox') {
      // hide saved badge
      document.querySelectorAll(".saved").forEach(x => x.style.visibility = "hidden");
      document.querySelectorAll(".source").forEach(x => x.style.background = "rgb(255, 235, 195)");

      // Clear the previous debounce timer
      clearTimeout(debounceTimer);

      // Set a new debounce timer to delay the form submission
      debounceTimer = setTimeout(() => {
        // As soon as the user stops changing checkboxes, submit *that* form.
        submitChecklistForm(form);
      }, DEBOUNCE_DELAY);
    }
  });

  // prevent standard full page reload
  form.addEventListener('submit', e => {
    e.preventDefault();
    submitChecklistForm(form);
  });

});