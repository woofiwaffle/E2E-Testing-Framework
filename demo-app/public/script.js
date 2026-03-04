// -------------------- Boot --------------------


/* -------------------- Theme toggle -------------------- */
const THEME_KEY = 'demo.theme';

(function initTheme() {
  try {
    const savedTheme = localStorage.getItem(THEME_KEY);
    if (savedTheme === 'dark') {
      document.body.classList.add('dark-theme');
    }
  } catch (e) {
  }
})();

window.addEventListener('load', () => {
  const themeToggle = document.getElementById('theme-toggle');
  if (!themeToggle) return;

  themeToggle.addEventListener('click', () => {
    const isDark = document.body.classList.toggle('dark-theme');
    try {
      localStorage.setItem(THEME_KEY, isDark ? 'dark' : 'light');
    } catch (e) {
    }
  });
});


window.addEventListener('load', () => {

  /* -------------------- DOM elements -------------------- */
  const btn = document.getElementById('demo-button');
  const input = document.getElementById('demo-input');
  const result = document.getElementById('result');
  const modal = document.getElementById('demo-modal');
  const openModalBtn = document.getElementById('open-modal');
  const closeModalBtn = document.querySelector('.close');
  const showToastBtn = document.getElementById('show-toast');
  const toast = document.getElementById('demo-toast');


  /* -------------------- Send to server functionality -------------------- */
  btn.addEventListener('click', async () => {
    const text = input.value.trim();
    if (!text) {
      result.textContent = 'Please enter some text';
      return;
    }
    try {
      const resp = await fetch('/api/echo', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
      });
      const data = await resp.json();
      if (resp.ok) {
        result.textContent = data.data || '(empty)';
      } else {
        result.textContent = `Error: ${data.message}`;
      }
    } catch (err) {
      result.textContent = 'Error: ' + err.message;
    }
  });


  /* -------------------- Modal functionality -------------------- */
  openModalBtn.addEventListener('click', () => {
    modal.style.display = 'block';
  });

  closeModalBtn.addEventListener('click', () => {
    modal.style.display = 'none';
  });

  window.addEventListener('click', (event) => {
    if (event.target === modal) {
      modal.style.display = 'none';
    }
  });


  /* -------------------- Toast functionality -------------------- */
  showToastBtn.addEventListener('click', () => {
    toast.classList.add('show');
    setTimeout(() => {
      toast.classList.remove('show');
    }, 3000);
  });


  /* -------------------- Simple form functionality -------------------- */
  const simpleForm = document.getElementById('simple-form');
  const loadingIndicator = document.getElementById('loading-indicator');
  if (simpleForm) {
    simpleForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const input = document.getElementById('simple-input').value.trim();

      if (!input) {
        result.textContent = 'Please enter some text';
        return;
      }

      try {
        loadingIndicator.style.display = 'block';
        const resp = await fetch('/api/echo', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ text: input })
        });
        const data = await resp.json();
        if (resp.ok) {
          result.textContent = `Form submitted successfully: ${data.data}`;
          document.getElementById('simple-input').value = '';
        } else {
          result.textContent = `Error: ${data.message}`;
        }
      } catch (err) {
        result.textContent = 'Error: ' + err.message;
      } finally {
        loadingIndicator.style.display = 'none';
      }
    });
  }


  /* -------------------- Simple list functionality -------------------- */
  async function loadSimpleList() {
    try {
      const resp = await fetch('/api/items');
      const data = await resp.json();
      const list = document.getElementById('simple-list');
      list.innerHTML = '';
      data.data.forEach(item => {
        const listItem = document.createElement('li');
        listItem.innerHTML = `
          <span>${item.id}: ${item.name}</span>
          <div class="list-item-btns">
            <button class="edit-btn" data-id="${item.id}">Edit</button>
            <button class="delete-btn" data-id="${item.id}">Delete</button>
          </div>
        `;
        list.appendChild(listItem);
      });
      document.querySelectorAll('.edit-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
          const id = e.target.getAttribute('data-id');
          const name = e.target.parentElement.previousElementSibling.textContent.split(': ')[1];
          editItem(parseInt(id), name);
        });
      });
      document.querySelectorAll('.delete-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
          const id = parseInt(e.target.getAttribute('data-id'));
          deleteItem(id);
        });
      });
    } catch (err) {
    }
  }

  async function addItem(name) {
    try {
      const resp = await fetch('/api/items', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name })
      });
      const data = await resp.json();
      if (resp.ok) {
        result.textContent = `Item added successfully: ${data.data.name}`;
        loadSimpleList();
      } else {
        result.textContent = `Error: ${data.message}`;
      }
    } catch (err) {
      result.textContent = 'Error: ' + err.message;
    }
  }

  async function deleteItem(id) {
    try {
      const resp = await fetch(`/api/items/${id}`, { method: 'DELETE' });
      const data = await resp.json();
      if (resp.ok) {
        result.textContent = `Item deleted successfully`;
        loadSimpleList();
      } else {
        result.textContent = `Error: ${data.message}`;
      }
    } catch (err) {
      result.textContent = 'Error: ' + err.message;
    }
  }

  async function editItem(id, currentName) {
    try {
      const newName = await window.customPrompt('Enter new name:', currentName);
      if (newName === null) {
        return; 
      }
      if (!newName.trim() || newName.trim() === currentName) {
        return;
      }

      const resp = await fetch(`/api/items/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: newName.trim() })
      });
      const data = await resp.json();
      if (resp.ok) {
        result.textContent = `Item updated successfully: ${data.data.name}`;
        loadSimpleList();
      } else {
        result.textContent = `Error: ${data.message}`;
      }
    } catch (err) {
      result.textContent = 'Error: ' + err.message;
    }
  }

  window.customPrompt = function(message, defaultValue) {

    const modal = document.createElement('div');
    modal.className = 'custom-prompt-modal';
    modal.style.display = 'flex';

    const promptBox = document.createElement('div');
    promptBox.className = 'custom-prompt-box';

    const promptMessage = document.createElement('p');
    promptMessage.className = 'custom-prompt-message';
    promptMessage.textContent = message;

    const promptInput = document.createElement('input');
    promptInput.className = 'custom-prompt-input';
    promptInput.type = 'text';
    promptInput.value = defaultValue;

    const promptButtons = document.createElement('div');
    promptButtons.className = 'custom-prompt-buttons';

    const okButton = document.createElement('button');
    okButton.textContent = 'OK';

    const cancelButton = document.createElement('button');
    cancelButton.textContent = 'Cancel';

    promptButtons.appendChild(okButton);
    promptButtons.appendChild(cancelButton);

    promptBox.appendChild(promptMessage);
    promptBox.appendChild(promptInput);
    promptBox.appendChild(promptButtons);

    modal.appendChild(promptBox);
    document.body.appendChild(modal);

    return new Promise((resolve) => {
      okButton.addEventListener('click', () => {
        const value = promptInput.value;
        document.body.removeChild(modal);
        resolve(value);
      });

      cancelButton.addEventListener('click', () => {
        document.body.removeChild(modal);
        resolve(null);
      });
    });
  };

  const addItemBtn = document.getElementById('add-item-btn');
  if (addItemBtn) {
    addItemBtn.addEventListener('click', () => {
      const newItemInput = document.getElementById('new-item-input');
      const name = newItemInput.value.trim();
      if (!name) {
        result.textContent = 'Please enter a name';
        return;
      }
      addItem(name);
      newItemInput.value = '';
    });
  }

  loadSimpleList();
});
