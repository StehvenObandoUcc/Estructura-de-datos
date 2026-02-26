export type CommandType = "MOVE" | "GRIP" | "WELD" | "INSPECT" | "RELEASE";
export type CommandStatus = "QUEUED" | "DONE";

export class RobotCommand {
    status: CommandStatus = "QUEUED";

    constructor(
        public commandId: string,
        public commandType: CommandType,
        public joint: string,
        public detail: string
    ) { }

    toString(): string {
        return `${this.commandId} | ${this.commandType} | ${this.joint} | ${this.detail}`;
    }
}
