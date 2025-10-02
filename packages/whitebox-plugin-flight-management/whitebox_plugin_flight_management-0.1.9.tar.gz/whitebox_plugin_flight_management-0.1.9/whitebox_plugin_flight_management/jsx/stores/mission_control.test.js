import useMissionControlStore from "./mission_control";

describe('useMissionControlStore', () => {
  const getState = useMissionControlStore.getState;
  const setState = useMissionControlStore.setState;

  let socketsSendMock;
  let apiGetPathMock;
  let apiClientGetMock;

  beforeEach(async () => {
    socketsSendMock = vi.fn();
    apiGetPathMock = vi.fn();
    apiClientGetMock = vi.fn();

    globalThis.Whitebox = {
      sockets: {
        send: socketsSendMock,
        addEventListener: vi.fn(),
      },
      api: {
        getPluginProvidedPath: apiGetPathMock,
        client: {
          get: apiClientGetMock,
        },
      },
    };

    // Dynamically import the module under test (ensures it reads our Whitebox)
    vi.resetModules();
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  describe('helpers', () => {
    it('setFlightSession/getFlightSession and isFlightSessionActive', () => {
      const s = getState();
      expect(s.isLoaded).toBe(false);
      expect(s.getFlightSession()).toBe(null);
      expect(s.isFlightSessionActive()).toBeFalsy();

      const active = {id: 1, started_at: '2025-01-01T00:00:00Z', ended_at: null};
      s.setFlightSession(active);
      expect(getState().isLoaded).toBe(true);
      expect(getState().getFlightSession()).toEqual(active);
      expect(getState().isFlightSessionActive()).toBe(true);

      const ended = {...active, ended_at: '2025-01-01T01:00:00Z'};
      getState().setFlightSession(ended);
      expect(getState().isFlightSessionActive()).toBeFalsy();
    });
  });

  describe('flight session management', () => {
    it('startFlightSession sends socket message and flips isLoaded to false', async () => {
      // Make it true first so we see it flip to false
      getState().setFlightSession({id: 1, ended_at: null});

      await getState().startFlightSession();
      expect(getState().isLoaded).toBe(false);
      expect(socketsSendMock).toHaveBeenCalledWith('flight', {type: 'flight.start'});
    });

    it('endFlightSession sends socket message and flips isLoaded to false', async () => {
      // Make it true first so we see it flip to false
      getState().setFlightSession({id: 1, ended_at: null});

      await getState().endFlightSession();
      expect(getState().isLoaded).toBe(false);
      expect(socketsSendMock).toHaveBeenCalledWith('flight', {type: 'flight.end'});
    });

    it('toggleFlightSession calls end when active and start when not active', async () => {
      socketsSendMock.mockClear();

      // Active session -> should end
      getState().setFlightSession({id: 1, ended_at: null});
      await getState().toggleFlightSession();
      expect(socketsSendMock).toHaveBeenLastCalledWith('flight', {type: 'flight.end'});

      // Ended session -> should start
      getState().setFlightSession({id: 1, ended_at: '2025-01-01T01:00:00Z'});
      await getState().toggleFlightSession();
      expect(socketsSendMock).toHaveBeenLastCalledWith('flight', {type: 'flight.start'});

      // No session -> should start
      setState({flightSession: null});
      await getState().toggleFlightSession();
      expect(socketsSendMock).toHaveBeenLastCalledWith('flight', {type: 'flight.start'});
    });
  });

  describe('flight sessions fetching', () => {
    it('fetchFlightSessions success sets data and state', async () => {
      const fakeUrl = '/api/flight-sessions';
      const payload = [{id: 1}, {id: 2}];
      apiGetPathMock.mockReturnValue(fakeUrl);
      apiClientGetMock.mockResolvedValue({data: payload});

      const ok = await getState().fetchFlightSessions();
      // expect(ok).toBe(true);
      expect(apiGetPathMock).toHaveBeenCalledWith('flight.flight-session-list');
      expect(getState().flightSessions).toEqual(payload);
      expect(getState().fetchState).toBe('loaded');

      // getFlightSessions returns [] if null, otherwise the array as-is
      expect(getState().getFlightSessions()).toEqual(payload);
      setState({flightSessions: null});
      expect(getState().getFlightSessions()).toEqual([]);
    });

    it('fetchFlightSessions failure sets fetchState=error and returns false', async () => {
      apiGetPathMock.mockReturnValue('/api/flight-sessions');
      apiClientGetMock.mockRejectedValue(new Error('boom'));

      const ok = await getState().fetchFlightSessions();
      expect(ok).toBe(false);
      expect(getState().fetchState).toBe('error');
    });
  });

  describe('playback controls', () => {
    it('play/pause emit corresponding events and toggle state', () => {
      const events = [];
      const unsub = getState().on('player.play', () => events.push('play'));
      const unsub2 = getState().on('player.pause', () => events.push('pause'));

      expect(getState().playbackIsPlaying).toBe(false);

      getState().playbackPlay();
      expect(getState().playbackIsPlaying).toBe(true);

      getState().playbackPause();
      expect(getState().playbackIsPlaying).toBe(false);

      expect(events).toEqual(['play', 'pause']);

      unsub();
      unsub2();
    });

    it('playbackToggle switches between play and pause', () => {
      setState({playbackIsPlaying: false});
      getState().playbackToggle();
      expect(getState().playbackIsPlaying).toBe(true);
      getState().playbackToggle();
      expect(getState().playbackIsPlaying).toBe(false);
    });

    it('setPlaybackTime clamps and emits "player.time"', () => {
      const session = {
        started_at: '2025-01-01T00:00:00Z',
        ended_at: '2025-01-01T00:01:40Z', // 100s total
      };
      setState({playbackFlightSession: session});

      const times = [];
      const unsub = getState().on('player.time', (t) => times.push(t));

      // within range
      getState().setPlaybackTime(42);
      expect(getState().playbackTime).toBe(42);

      // below range
      getState().setPlaybackTime(-5);
      expect(getState().playbackTime).toBe(0);

      // above range (clamp to 100)
      getState().setPlaybackTime(150);
      expect(getState().playbackTime).toBe(100);

      expect(times).toEqual([42, 0, 100]);
      unsub();
    });
  });

  describe('mode slice', () => {
    it('enterFlightMode sets mode and clears playbackFlightSession', () => {
      setState({
        mode: 'playback',
        playbackFlightSession: {id: 7},
      });
      getState().enterFlightMode();
      expect(getState().mode).toBe('flight');
      expect(getState().playbackFlightSession).toBeNull();
    });

    it('enterPlaybackMode sets mode and session; calls playbackReset when switching from non-playback', () => {
      // inject a spy into state for playbackReset
      const spy = vi.fn();
      setState({mode: 'flight', playbackReset: spy});

      const fs = {id: 99, started_at: '2025-01-01T00:00:00Z', ended_at: '2025-01-01T00:10:00Z'};
      getState().enterPlaybackMode(fs);

      expect(spy).toHaveBeenCalledTimes(1);
      expect(getState().mode).toBe('playback');
      expect(getState().playbackFlightSession).toEqual(fs);
    });

    it('enterPlaybackMode does NOT call playbackReset when already in playback', () => {
      const spy = vi.fn();
      setState({mode: 'playback', playbackReset: spy});

      getState().enterPlaybackMode({id: 1});
      expect(spy).not.toHaveBeenCalled();
    });
  });

})
