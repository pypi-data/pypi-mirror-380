import { Component, OnDestroy } from "@angular/core";
import { PwaVersionCheckerService } from "@peek/peek_core_device";
import { BehaviorSubject } from "rxjs";
import { NgLifeCycleEvents } from "@synerty/vortexjs";
import { takeUntil } from "rxjs/operators";

@Component({
    selector: "pwa-app-version-checker-component",
    templateUrl: "./pwa-version-checker.component.html",
    styleUrls: ["./pwa-version-checker.component.scss"],
})
export class PwaVersionCheckerComponent
    extends NgLifeCycleEvents
    implements OnDestroy
{
    isVisible: boolean = true;
    countdown: number = 5;
    private countdownInterval?: number;

    constructor(public pwaVersionCheckerService: PwaVersionCheckerService) {
        super();
        pwaVersionCheckerService.isNewVersionAvailable$
            .pipe(takeUntil(this.onDestroyEvent))
            .subscribe((hasUpdate: boolean) => {
                if (hasUpdate) {
                    this.startCountdown();
                } else {
                    this.clearCountdown();
                }
            });
        this.onDestroyEvent.subscribe(() => this.clearCountdown());
    }

    applyUpdate(): void {
        this.clearCountdown();
        this.pwaVersionCheckerService.applyUpdate();
    }

    get hasUpdate$(): BehaviorSubject<boolean> {
        return this.pwaVersionCheckerService.isNewVersionAvailable$;
    }

    private startCountdown(): void {
        this.countdownInterval = window.setInterval(() => {
            this.countdown--;
            if (this.countdown <= 0) {
                this.applyUpdate();
            }
        }, 1000);
    }

    private clearCountdown(): void {
        if (this.countdownInterval) {
            clearInterval(this.countdownInterval);
            this.countdownInterval = undefined;
        }
    }
}
