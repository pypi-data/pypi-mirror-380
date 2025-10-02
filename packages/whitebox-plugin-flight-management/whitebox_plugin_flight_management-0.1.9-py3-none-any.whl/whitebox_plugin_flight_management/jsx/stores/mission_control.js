import { create } from "zustand";

const { createEventHandlingSlice } = Whitebox.utils;

const createFlightSessionControlSlice = (set, get) => ({
  isLoaded: false,
  flightSession: null,

  // region helpers

  setFlightSession: (session) => {
    set({
      flightSession: session,
      isLoaded: true,
    });
  },

  getFlightSession: () => {
    return get().flightSession;
  },

  isFlightSessionActive: () => {
    const flightSession = get().flightSession;
    return flightSession && flightSession.ended_at === null;
  },

  // endregion helpers

  // region flight session management

  startFlightSession: async () => {
    set({ isLoaded: false });

    const data = {
      type: "flight.start",
    };
    Whitebox.sockets.send("flight", data);
  },

  endFlightSession: async () => {
    set({ isLoaded: false });

    const data = {
      type: "flight.end",
    };
    Whitebox.sockets.send("flight", data);
  },

  toggleFlightSession: async () => {
    const flightSession = get().flightSession;

    if (flightSession && flightSession.ended_at === null) {
      await get().endFlightSession();
    } else {
      await get().startFlightSession();
    }
  },

  // endregion flight session management
});

const createFlightManagementSlice = (set, get) => ({
  fetchState: "initial",
  flightSessions: null,

  fetchFlightSessions: async () => {
    const { api } = Whitebox;

    const url = api.getPluginProvidedPath("flight.flight-session-list");
    let data = null;

    try {
      const response = await api.client.get(url);
      data = response.data;
    } catch (e) {
      console.error("Failed to fetch flight sessions", e);
      set({ fetchState: "error" });
      return false;
    }

    set({
      flightSessions: data,
      fetchState: "loaded",
    });
    return true;
  },

  getFlightSessions: () => {
    const flightSessions = get().flightSessions;

    if (flightSessions === null) {
      return [];
    }
    return flightSessions;
  },
})

const createFlightPlaybackSlice = (set, get) => ({
  playbackFlightSession: null,
  playbackIsPlaying: false,
  playbackTime: 0,

  playbackPlay: () => {
    const { emit } = get();
    set({ playbackIsPlaying: true });
    emit("player.play");
  },
  playbackPause: () => {
    const { emit } = get();
    set({ playbackIsPlaying: false });
    emit("player.pause");
  },
  playbackToggle: () => {
    const { playbackIsPlaying } = get();
    if (playbackIsPlaying) {
      get().playbackPause();
    } else {
      get().playbackPlay();
    }
  },

  setPlaybackTime: (time) => {
    const {
      playbackFlightSession,
      emit,
    } = get();

    const startedAt = new Date(playbackFlightSession.started_at);
    const endedAt = new Date(playbackFlightSession.ended_at);
    const totalDuration = (endedAt.getTime() - startedAt.getTime()) / 1000;

    let timeToAssign = time;

    if (time < 0) {
      timeToAssign = 0;
    } else if (time > totalDuration) {
      timeToAssign = totalDuration;
    }

    set({ playbackTime: timeToAssign });
    emit("player.time", timeToAssign);
  },

  playbackReset: () => {},
})

const createModeSlice = (set, get) => ({
  // On load, we should be in flight mode
  mode: "flight",

  enterFlightMode: () => set({
    mode: "flight",
    playbackFlightSession: null,
  }),
  enterPlaybackMode: (flightSession) => {
    const {
      mode,
      playbackReset,
    } = get();

    if (mode !== "playback") {
      playbackReset();
    }

    set({
      mode: "playback",
      playbackFlightSession: flightSession,
    });
  },
});

const useMissionControlStore = create((...a) => ({
  ...createFlightSessionControlSlice(...a),
  ...createFlightManagementSlice(...a),
  ...createFlightPlaybackSlice(...a),
  ...createModeSlice(...a),
  ...createEventHandlingSlice(...a),
}));

export default useMissionControlStore;
