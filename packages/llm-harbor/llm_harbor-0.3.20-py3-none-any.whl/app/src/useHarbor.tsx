import { useCallback, useEffect, useState } from "react";
import { ChildProcess, Command } from "@tauri-apps/plugin-shell";
import { join } from "@tauri-apps/api/path";

import { isWindows, once, resolveResultLines } from "./utils";
import { PROFILES_DIR } from "./configMetadata";

export const resolveHarborHome = once(async function __resolveHarborHome() {
    const result = await runHarbor(["home"]);
    const path = resolveResultLines(result).join('\n');

    if (await isWindows()) {
        // On windows, we need to resolve the path first via WSL
        const wslResult = await Command.create("wsl.exe", ["-e", "wslpath", "-w", path]).execute();
        return resolveResultLines(wslResult).join('\n');
    }

    return path;
});

export const resolveProfilesDir = once(async function __resolveProfilesDir() {
    const homeDir = await resolveHarborHome();
    return await join(homeDir, PROFILES_DIR);
});

export async function runHarbor(args: string[]) {
    if (await isWindows()) {
        return await Command.create("wsl.exe", ["-e", "bash", "-lic", `harbor ${args.join(' ')}`]).execute();
    } else {
        return await Command.create("harbor", args).execute();
    }
}

export const useHarborTrigger = (args: string[]) => {
    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState<ChildProcess<string> | null>(null);
    const [error, setError] = useState<Error | null>(null);

    const runCommand = useCallback(
        async () => {
            setLoading(true);
            setError(null);

            try {
                const result = await runHarbor(args);
                setResult(result);
            } catch (e) {
                if (e instanceof Error) {
                    setError(e);
                } else {
                    setError(new Error(`Unexpected error: ${e}`));
                }
            } finally {
                setLoading(false);
            }
        },
        args,
    );

    const run = useCallback(() => {
        runCommand();
    }, [runCommand]);

    return {
        loading,
        error,
        result,
        run,
    };
};

/**
 * Run Harbor Shell command and return the result
 */
export const useHarbor = (args: string[]) => {
    const { run, ...rest } = useHarborTrigger(args);

    useEffect(() => {
        run();
    }, [run, ...args]);

    return {
        ...rest,
        rerun: run,
    };
};
