import { RobotCommand } from "./RobotCommand.js";

export class RobotArmQueue {
    private items: RobotCommand[] = [];

    enQueue(cmd: RobotCommand): void { this.items.push(cmd); }
    deQueue(): RobotCommand | undefined { return this.items.shift(); }
    front(): RobotCommand | undefined { return this.items[0]; }
    rear(): RobotCommand | undefined { return this.items[this.items.length - 1]; }
    size(): number { return this.items.length; }
    isEmpty(): boolean { return this.items.length === 0; }
    getAll(): RobotCommand[] { return [...this.items]; }
}
