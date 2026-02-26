import { RobotCommand, CommandType } from "./RobotCommand.js";
import { RobotArmQueue } from "./RobotArmQueue.js";

// ─── Instancia ───────────────────────────────────────────────────────────────
const armQueue = new RobotArmQueue();

armQueue.enQueue(new RobotCommand("CMD-001", "MOVE", "Axis-Z", "Extend 80mm"));
armQueue.enQueue(new RobotCommand("CMD-002", "GRIP", "Gripper", "Close grip"));
armQueue.enQueue(new RobotCommand("CMD-003", "WELD", "Joint-A1", "Apply 3kN"));
armQueue.enQueue(new RobotCommand("CMD-004", "INSPECT", "Camera", "Scan weld"));
armQueue.enQueue(new RobotCommand("CMD-005", "RELEASE", "Gripper", "Open grip"));

// ─── Helpers de DOM ───────────────────────────────────────────────────────────
const el = (id: string): HTMLElement => document.getElementById(id)!;

function renderQueue(): void {
  const list = el("queue-list");
  list.innerHTML = "";

  if (armQueue.isEmpty()) {
    list.innerHTML = "<p>✅ All commands executed.</p>";
    el("counter").textContent = "Commands in queue: 0";
    return;
  }

  armQueue.getAll().forEach((cmd, i) => {
    const card = document.createElement("div");
    card.className = `card${i === 0 ? " next" : ""}`;
    card.innerHTML = `
      ${i === 0 ? '<span class="next-label">▶ NEXT</span>' : ""}
      <strong>${cmd.commandId}</strong> | ${cmd.commandType} | ${cmd.joint} | ${cmd.detail} | <em>${cmd.status}</em>
    `;
    list.appendChild(card);
  });

  el("counter").textContent = `Commands in queue: ${armQueue.size()}`;
}

function executeNext(): void {
  const cmd = armQueue.deQueue();
  if (!cmd) { alert("Queue is empty!"); return; }
  cmd.status = "DONE";

  const entry = document.createElement("div");
  entry.className = "log-entry";
  entry.textContent = `✅ ${cmd.toString()} → DONE`;

  el("log-list").prepend(entry); // más reciente arriba
  renderQueue();
}

function addCommand(): void {
  const id = (el("inp-id") as HTMLInputElement).value.trim();
  const type = (el("inp-type") as HTMLSelectElement).value as CommandType;
  const joint = (el("inp-joint") as HTMLInputElement).value.trim();
  const detail = (el("inp-detail") as HTMLInputElement).value.trim();

  if (!id || !joint || !detail) { alert("All fields are required!"); return; }

  armQueue.enQueue(new RobotCommand(id, type, joint, detail));

  (el("inp-id") as HTMLInputElement).value = "";
  (el("inp-joint") as HTMLInputElement).value = "";
  (el("inp-detail") as HTMLInputElement).value = "";

  el("form-container").style.display = "none";
  renderQueue();
}

// ─── Event Listeners ──────────────────────────────────────────────────────────
renderQueue();

el("btn-execute").addEventListener("click", executeNext);
el("btn-submit").addEventListener("click", addCommand);
el("btn-toggle-form").addEventListener("click", () => {
  const form = el("form-container");
  form.style.display = form.style.display === "none" ? "block" : "none";
});
