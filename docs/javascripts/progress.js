(function () {
  const key = "agents-from-scratch-progress";
  const read = () => JSON.parse(localStorage.getItem(key) || "[]");
  const write = (items) => localStorage.setItem(key, JSON.stringify([...new Set(items)]));
  function render() {
    const items = read();
    document.querySelectorAll("[data-progress-count]").forEach((el) => el.textContent = items.length);
    document.querySelectorAll("[data-progress-bar]").forEach((el) => el.style.width = `${Math.min(100, items.length * 5)}%`);
    document.querySelectorAll("[data-progress-reset]").forEach((el) => el.onclick = () => { localStorage.removeItem(key); render(); });
  }
  document.addEventListener("click", (event) => {
    const box = event.target.closest(".task-list-item-checkbox");
    if (!box) return;
    const match = location.pathname.match(/lesson-(\d{2})/);
    if (!match) return;
    const items = read();
    if (box.checked) items.push(match[1]); else write(items.filter((item) => item !== match[1]));
    write(items); render();
  });
  document.addEventListener("DOMContentLoaded", render);
  render();
})();
