import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { SwUpdate, VersionEvent } from "@angular/service-worker";
import { BehaviorSubject, interval, of, Subject, throttleTime } from "rxjs";
import { catchError, takeUntil } from "rxjs/operators";

@Injectable()
export class PwaVersionCheckerService {
    readonly isNewVersionAvailable$ = new BehaviorSubject<boolean>(false);
    private readonly _isPwaInstalled$ = new BehaviorSubject<boolean>(false);

    private readonly CHECK_INTERVAL_MILLISECONDS: number = 60 * 60 * 1000;
    private readonly LOGIN_CHECK_INTERVAL_MILLISECONDS: number = 60 * 1000;
    private unsub = new Subject<void>();

    constructor(
        private swUpdate: SwUpdate,
        private http: HttpClient,
    ) {
        this.setIsPwaInstalled(this.swUpdate.isEnabled);

        this.checkLoginRedirect();
        this.setupLoginRedirectCheck();

        if (!this.isPwaInstalled) {
            return;
        }

        this.checkForUpdateOnce();
        this.setupCheckForUpdates();
    }

    get isPwaInstalled(): boolean {
        return this._isPwaInstalled$.getValue();
    }

    get isPwaInstalled$() {
        return this._isPwaInstalled$.asObservable();
    }

    private setIsPwaInstalled(value: boolean): void {
        this._isPwaInstalled$.next(value);
    }

    private checkForUpdateOnce(): void {
        if (!this.isPwaInstalled) {
            return;
        }

        this.swUpdate.checkForUpdate().then((hasUpdate: boolean) => {
            if (hasUpdate) {
                this.isNewVersionAvailable$.next(true);
            }
        });
    }

    setupCheckForUpdates(): void {
        this.unsub.next();

        if (!this.isPwaInstalled) {
            return;
        }

        this.swUpdate.versionUpdates
            .pipe(takeUntil(this.unsub))
            .pipe(throttleTime(this.CHECK_INTERVAL_MILLISECONDS))
            .subscribe((evt: VersionEvent) => {
                if (!this.isPwaInstalled) {
                    return;
                }

                switch (evt.type) {
                    case "VERSION_DETECTED":
                        console.log(
                            `PwaVersionCheckerService:` +
                                ` Downloading new app version: ` +
                                `${evt.version.hash}`,
                        );
                        break;
                    case "VERSION_READY":
                        console.log(
                            `PwaVersionCheckerService:` +
                                ` Current app version: ` +
                                `${evt.currentVersion.hash}`,
                        );
                        console.log(
                            `PwaVersionCheckerService:` +
                                ` New app version ready for use: ` +
                                `${evt.latestVersion.hash}`,
                        );
                        this.isNewVersionAvailable$.next(true);
                        break;
                    case "VERSION_INSTALLATION_FAILED":
                        console.log(
                            `Failed to install app version ` +
                                `'${evt.version.hash}': ${evt.error}`,
                        );
                        break;
                }
            });
    }

    private setupLoginRedirectCheck(): void {
        interval(this.LOGIN_CHECK_INTERVAL_MILLISECONDS)
            .pipe(takeUntil(this.unsub))
            .subscribe(() => {
                this.checkLoginRedirect();
            });
    }

    private checkLoginRedirect(): void {
        console.log("PwaVersionCheckerService: checkLoginRedirect called");
        this.http
            .get("/peek_core_device/assets/pwa-login-check.json", {
                observe: "response",
                responseType: "json",
            })
            .pipe(
                catchError((error) => {
                    console.log(
                        `PwaVersionCheckerService: ` + `code: ${error?.status}`,
                    );
                    if (error?.status == 0 || error?.status == 302) {
                        const redirectUrl = error.headers.get("Location");
                        if (redirectUrl) {
                            console.log(
                                `PwaVersionCheckerService: Redirecting to ` +
                                    `${redirectUrl}`,
                            );
                            window.location.href = redirectUrl;
                        } else {
                            console.log(
                                `PwaVersionCheckerService: Reloading page`,
                            );
                            document.location.reload();
                        }
                    }
                    return of(error);
                }),
            )
            .subscribe((response) => {
                console.log(
                    "PwaVersionCheckerService: checkLoginRedirect:" +
                        ` Login fetch status code: ${response?.status}`,
                );
            });
    }

    applyUpdate(): void {
        document.location.reload();
    }
}
