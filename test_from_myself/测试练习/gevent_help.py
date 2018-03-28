import gevent 

help(gevent)
"""
Help on package gevent:

NAME
    gevent

DESCRIPTION
    gevent is a coroutine-based Python networking library that uses greenlet
    to provide a high-level synchronous API on top of libev event loop.
    
    See http://www.gevent.org/ for the documentation.

PACKAGE CONTENTS
    _compat
    _fileobjectcommon
    _fileobjectposix
    _semaphore
    _socket2
    _socket3
    _socketcommon
    _ssl2
    _ssl3
    _sslgte279
    _tblib
    _threading
    _util
    _util_py2
    backdoor
    baseserver
    builtins
    core
    event
    fileobject
    greenlet
    hub
    libev (package)
    local
    lock
    monkey
    os
    pool
    pywsgi
    queue
    resolver_ares
    resolver_thread
    select
    server
    signal
    socket
    ssl
    subprocess
    thread
    threading
    threadpool
    timeout
    util
    win32util
    wsgi

SUBMODULES
    _signal_module

CLASSES
    builtins.BaseException(builtins.object)
        gevent.timeout.Timeout
        greenlet.GreenletExit
    builtins.object
        signal
    greenlet.greenlet(builtins.object)
        gevent.greenlet.Greenlet
    
    class Greenlet(greenlet.greenlet)
     |  A light-weight cooperatively-scheduled execution unit.
     |  
     |  Method resolution order:
     |      Greenlet
     |      greenlet.greenlet
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __bool__(self)
     |      self != 0
     |  
     |  __init__(self, run=None, *args, **kwargs)
     |      Greenlet constructor.
     |      
     |      :param args: The arguments passed to the ``run`` function.
     |      :param kwargs: The keyword arguments passed to the ``run`` function.
     |      :keyword run: The callable object to run. If not given, this object's
     |          `_run` method will be invoked (typically defined by subclasses).
     |      
     |      .. versionchanged:: 1.1b1
     |          The ``run`` argument to the constructor is now verified to be a callable
     |          object. Previously, passing a non-callable object would fail after the greenlet
     |          was spawned.
     |  
     |  __nonzero__ = __bool__(self)
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  get(self, block=True, timeout=None)
     |      Return the result the greenlet has returned or re-raise the exception it has raised.
     |      
     |      If block is ``False``, raise :class:`gevent.Timeout` if the greenlet is still alive.
     |      If block is ``True``, unschedule the current greenlet until the result is available
     |      or the timeout expires. In the latter case, :class:`gevent.Timeout` is raised.
     |  
     |  join(self, timeout=None)
     |      Wait until the greenlet finishes or *timeout* expires.
     |      Return ``None`` regardless.
     |  
     |  kill(self, exception=<class 'greenlet.GreenletExit'>, block=True, timeout=None)
     |      Raise the ``exception`` in the greenlet.
     |      
     |      If ``block`` is ``True`` (the default), wait until the greenlet dies or the optional timeout expires.
     |      If block is ``False``, the current greenlet is not unscheduled.
     |      
     |      The function always returns ``None`` and never raises an error.
     |      
     |      .. note::
     |      
     |          Depending on what this greenlet is executing and the state
     |          of the event loop, the exception may or may not be raised
     |          immediately when this greenlet resumes execution. It may
     |          be raised on a subsequent green call, or, if this greenlet
     |          exits before making such a call, it may not be raised at
     |          all. As of 1.1, an example where the exception is raised
     |          later is if this greenlet had called :func:`sleep(0)
     |          <gevent.sleep>`; an example where the exception is raised
     |          immediately is if this greenlet had called
     |          :func:`sleep(0.1) <gevent.sleep>`.
     |      
     |      .. caution::
     |      
     |          Use care when killing greenlets. If the code executing is not
     |          exception safe (e.g., makes proper use of ``finally``) then an
     |          unexpected exception could result in corrupted state.
     |      
     |      See also :func:`gevent.kill`.
     |      
     |      :keyword type exception: The type of exception to raise in the greenlet. The default
     |          is :class:`GreenletExit`, which indicates a :meth:`successful` completion
     |          of the greenlet.
     |      
     |      .. versionchanged:: 0.13.0
     |          *block* is now ``True`` by default.
     |      .. versionchanged:: 1.1a2
     |          If this greenlet had never been switched to, killing it will prevent it from ever being switched to.
     |  
     |  link(self, callback, SpawnedLink=<class 'gevent.greenlet.SpawnedLink'>)
     |      Link greenlet's completion to a callable.
     |      
     |      The *callback* will be called with this instance as an
     |      argument once this greenlet is dead. A callable is called in
     |      its own :class:`greenlet.greenlet` (*not* a
     |      :class:`Greenlet`).
     |  
     |  link_exception(self, callback, SpawnedLink=<class 'gevent.greenlet.FailureSpawnedLink'>)
     |      Like :meth:`link` but *callback* is only notified when the greenlet dies because of an unhandled exception.
     |  
     |  link_value(self, callback, SpawnedLink=<class 'gevent.greenlet.SuccessSpawnedLink'>)
     |      Like :meth:`link` but *callback* is only notified when the greenlet
     |      has completed successfully.
     |  
     |  rawlink(self, callback)
     |      Register a callable to be executed when the greenlet finishes execution.
     |      
     |      The *callback* will be called with this instance as an argument.
     |      
     |      .. caution:: The callable will be called in the HUB greenlet.
     |  
     |  ready(self)
     |      Return a true value if and only if the greenlet has finished
     |      execution.
     |      
     |      .. versionchanged:: 1.1
     |          This function is only guaranteed to return true or false *values*, not
     |          necessarily the literal constants ``True`` or ``False``.
     |  
     |  run(self)
     |  
     |  start(self)
     |      Schedule the greenlet to run in this loop iteration
     |  
     |  start_later(self, seconds)
     |      Schedule the greenlet to run in the future loop iteration *seconds* later
     |  
     |  successful(self)
     |      Return a true value if and only if the greenlet has finished execution
     |      successfully, that is, without raising an error.
     |      
     |      .. tip:: A greenlet that has been killed with the default
     |          :class:`GreenletExit` exception is considered successful.
     |          That is, ``GreenletExit`` is not considered an error.
     |      
     |      .. note:: This function is only guaranteed to return true or false *values*,
     |            not necessarily the literal constants ``True`` or ``False``.
     |  
     |  throw(self, *args)
     |      Immediatelly switch into the greenlet and raise an exception in it.
     |      
     |      Should only be called from the HUB, otherwise the current greenlet is left unscheduled forever.
     |      To raise an exception in a safe manner from any greenlet, use :meth:`kill`.
     |      
     |      If a greenlet was started but never switched to yet, then also
     |      a) cancel the event that will start it
     |      b) fire the notifications as if an exception was raised in a greenlet
     |  
     |  unlink(self, callback)
     |      Remove the callback set by :meth:`link` or :meth:`rawlink`
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  spawn(*args, **kwargs) from builtins.type
     |      Create a new :class:`Greenlet` object and schedule it to run ``function(*args, **kwargs)``.
     |      This can be used as ``gevent.spawn`` or ``Greenlet.spawn``.
     |      
     |      The arguments are passed to :meth:`Greenlet.__init__`.
     |      
     |      .. versionchanged:: 1.1b1
     |          If a *function* is given that is not callable, immediately raise a :exc:`TypeError`
     |          instead of spawning a greenlet that will raise an uncaught TypeError.
     |  
     |  spawn_later(seconds, *args, **kwargs) from builtins.type
     |      Create and return a new Greenlet object scheduled to run ``function(*args, **kwargs)``
     |      in the future loop iteration *seconds* later. This can be used as ``Greenlet.spawn_later``
     |      or ``gevent.spawn_later``.
     |      
     |      The arguments are passed to :meth:`Greenlet.__init__`.
     |      
     |      .. versionchanged:: 1.1b1
     |         If an argument that's meant to be a function (the first argument in *args*, or the ``run`` keyword )
     |         is given to this classmethod (and not a classmethod of a subclass),
     |         it is verified to be callable. Previously, the spawned greenlet would have failed
     |         when it started running.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  dead
     |  
     |  exc_info
     |      Holds the exc_info three-tuple raised by the function if the
     |      greenlet finished with an error. Otherwise a false value.
     |      
     |      .. note:: This is a provisional API and may change.
     |      
     |      .. versionadded:: 1.1
     |  
     |  exception
     |      Holds the exception instance raised by the function if the greenlet has finished with an error.
     |      Otherwise ``None``.
     |  
     |  kwargs
     |  
     |  loop
     |  
     |  started
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  args = ()
     |  
     |  value = None
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from greenlet.greenlet:
     |  
     |  __getstate__(...)
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  getcurrent(...)
     |  
     |  gettrace(...)
     |  
     |  settrace(...)
     |  
     |  switch(...)
     |      switch(*args, **kwargs)
     |      
     |      Switch execution to this greenlet.
     |      
     |      If this greenlet has never been run, then this greenlet
     |      will be switched to using the body of self.run(*args, **kwargs).
     |      
     |      If the greenlet is active (has been run, but was switch()'ed
     |      out before leaving its run function), then this greenlet will
     |      be resumed and the return value to its switch call will be
     |      None if no arguments are given, the given argument if one
     |      argument is given, or the args tuple and keyword args dict if
     |      multiple arguments are given.
     |      
     |      If the greenlet is dead, or is the current greenlet then this
     |      function will simply return the arguments using the same rules as
     |      above.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from greenlet.greenlet:
     |  
     |  __dict__
     |  
     |  gr_frame
     |  
     |  parent
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from greenlet.greenlet:
     |  
     |  GreenletExit = <class 'greenlet.GreenletExit'>
     |      Common base class for all exceptions
     |  
     |  error = <class 'greenlet.error'>
     |      Common base class for all non-exit exceptions.
    
    class GreenletExit(builtins.BaseException)
     |  Common base class for all exceptions
     |  
     |  Method resolution order:
     |      GreenletExit
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class Timeout(builtins.BaseException)
     |  Raise *exception* in the current greenlet after given time period::
     |  
     |      timeout = Timeout(seconds, exception)
     |      timeout.start()
     |      try:
     |          ...  # exception will be raised here, after *seconds* passed since start() call
     |      finally:
     |          timeout.cancel()
     |  
     |  .. note:: If the code that the timeout was protecting finishes
     |     executing before the timeout elapses, be sure to ``cancel`` the
     |     timeout so it is not unexpectedly raised in the future. Even if
     |     it is raised, it is a best practice to cancel it. This
     |     ``try/finally`` construct or a ``with`` statement is a
     |     recommended pattern.
     |  
     |  When *exception* is omitted or ``None``, the :class:`Timeout` instance itself is raised:
     |  
     |      >>> import gevent
     |      >>> gevent.Timeout(0.1).start()
     |      >>> gevent.sleep(0.2)  #doctest: +IGNORE_EXCEPTION_DETAIL
     |      Traceback (most recent call last):
     |       ...
     |      Timeout: 0.1 seconds
     |  
     |  To simplify starting and canceling timeouts, the ``with`` statement can be used::
     |  
     |      with gevent.Timeout(seconds, exception) as timeout:
     |          pass  # ... code block ...
     |  
     |  This is equivalent to the try/finally block above with one additional feature:
     |  if *exception* is the literal ``False``, the timeout is still raised, but the context manager
     |  suppresses it, so the code outside the with-block won't see it.
     |  
     |  This is handy for adding a timeout to the functions that don't
     |  support a *timeout* parameter themselves::
     |  
     |      data = None
     |      with gevent.Timeout(5, False):
     |          data = mysock.makefile().readline()
     |      if data is None:
     |          ...  # 5 seconds passed without reading a line
     |      else:
     |          ...  # a line was read within 5 seconds
     |  
     |  .. caution:: If ``readline()`` above catches and doesn't re-raise :class:`BaseException`
     |     (for example, with a bare ``except:``), then your timeout will fail to function and control
     |     won't be returned to you when you expect.
     |  
     |  When catching timeouts, keep in mind that the one you catch may
     |  not be the one you have set (a calling function may have set its
     |  own timeout); if you going to silence a timeout, always check that
     |  it's the instance you need::
     |  
     |      timeout = Timeout(1)
     |      timeout.start()
     |      try:
     |          ...
     |      except Timeout as t:
     |          if t is not timeout:
     |              raise # not my timeout
     |  
     |  If the *seconds* argument is not given or is ``None`` (e.g.,
     |  ``Timeout()``), then the timeout will never expire and never raise
     |  *exception*. This is convenient for creating functions which take
     |  an optional timeout parameter of their own. (Note that this is not the same thing
     |  as a *seconds* value of 0.)
     |  
     |  .. caution::
     |     A *seconds* value less than 0.0 (e.g., -1) is poorly defined. In the future,
     |     support for negative values is likely to do the same thing as a value
     |     if ``None``.
     |  
     |  .. versionchanged:: 1.1b2
     |     If *seconds* is not given or is ``None``, no longer allocate a libev
     |     timer that will never be started.
     |  .. versionchanged:: 1.1
     |     Add warning about negative *seconds* values.
     |  
     |  Method resolution order:
     |      Timeout
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __enter__(self)
     |  
     |  __exit__(self, typ, value, tb)
     |  
     |  __init__(self, seconds=None, exception=None, ref=True, priority=-1, _use_timer=True)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  __str__(self)
     |      >>> raise Timeout #doctest: +IGNORE_EXCEPTION_DETAIL
     |      Traceback (most recent call last):
     |          ...
     |      Timeout
     |  
     |  cancel(self)
     |      If the timeout is pending, cancel it. Otherwise, do nothing.
     |  
     |  start(self)
     |      Schedule the timeout.
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  start_new(timeout=None, exception=None, ref=True) from builtins.type
     |      Create a started :class:`Timeout`.
     |      
     |      This is a shortcut, the exact action depends on *timeout*'s type:
     |      
     |      * If *timeout* is a :class:`Timeout`, then call its :meth:`start` method
     |        if it's not already begun.
     |      * Otherwise, create a new :class:`Timeout` instance, passing (*timeout*, *exception*) as
     |        arguments, then call its :meth:`start` method.
     |      
     |      Returns the :class:`Timeout` instance.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  pending
     |      Return True if the timeout is scheduled to be raised.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class signal(builtins.object)
     |  Cooperative implementation of special cases of :func:`signal.signal`.
     |  
     |  This module is designed to work with libev's child watchers, as used
     |  by default in :func:`gevent.os.fork` Note that each ``SIGCHLD`` handler
     |  will be run in a new greenlet when the signal is delivered (just like
     |  :class:`gevent.hub.signal`)
     |  
     |  The implementations in this module are only monkey patched if
     |  :func:`gevent.os.waitpid` is being used (the default) and if
     |  :const:`signal.SIGCHLD` is available; see :func:`gevent.os.fork` for
     |  information on configuring this not to be the case for advanced uses.
     |  
     |  .. versionadded:: 1.1b4
     |  
     |  Methods inherited from _signal_metaclass:
     |  
     |  default_int_handler(...)
     |      default_int_handler(...)
     |      
     |      The default handler for SIGINT installed by Python.
     |      It raises KeyboardInterrupt.
     |  
     |  getsignal(signalnum)
     |      Exactly the same as :func:`signal.signal` except where
     |      :const:`signal.SIGCHLD` is concerned.
     |      
     |      For :const:`signal.SIGCHLD`, this cooperates with :func:`signal`
     |      to provide consistent answers.
     |  
     |  set_wakeup_fd(...)
     |      set_wakeup_fd(fd) -> fd
     |      
     |      Sets the fd to be written to (with the signal number) when a signal
     |      comes in.  A library can use this to wakeup select or poll.
     |      The previous fd or -1 is returned.
     |      
     |      The fd must be non-blocking.
     |  
     |  signal(signalnum, handler)
     |      Exactly the same as :func:`signal.signal` except where
     |      :const:`signal.SIGCHLD` is concerned.
     |      
     |      .. note::
     |      
     |         A :const:`signal.SIGCHLD` handler installed with this function
     |         will only be triggered for children that are forked using
     |         :func:`gevent.os.fork` (:func:`gevent.os.fork_and_watch`);
     |         children forked before monkey patching, or otherwise by the raw
     |         :func:`os.fork`, will not trigger the handler installed by this
     |         function. (It's unlikely that a SIGCHLD handler installed with
     |         the builtin :func:`signal.signal` would be triggered either;
     |         libev typically overwrites such a handler at the C level. At
     |         the very least, it's full of race conditions.)
     |      
     |      .. note::
     |      
     |          Use of ``SIG_IGN`` and ``SIG_DFL`` may also have race conditions
     |          with libev child watchers and the :mod:`gevent.subprocess` module.
     |      
     |      .. versionchanged:: 1.2a1
     |           If ``SIG_IGN`` or ``SIG_DFL`` are used to ignore ``SIGCHLD``, a
     |           future use of ``gevent.subprocess`` and libev child watchers
     |           will once again work. However, on Python 2, use of ``os.popen``
     |           will fail.
     |      
     |      .. versionchanged:: 1.1rc2
     |           Allow using ``SIG_IGN`` and ``SIG_DFL`` to reset and ignore ``SIGCHLD``.
     |           However, this allows the possibility of a race condition if ``gevent.subprocess``
     |           had already been used.
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from _signal_metaclass:
     |  
     |  CTRL_BREAK_EVENT = <Signals.CTRL_BREAK_EVENT: 1>
     |  
     |  CTRL_C_EVENT = <Signals.CTRL_C_EVENT: 0>
     |  
     |  Handlers = <enum 'Handlers'>
     |      An enumeration.
     |  
     |  NSIG = 23
     |  
     |  SIGABRT = <Signals.SIGABRT: 22>
     |  
     |  SIGBREAK = <Signals.SIGBREAK: 21>
     |  
     |  SIGFPE = <Signals.SIGFPE: 8>
     |  
     |  SIGILL = <Signals.SIGILL: 4>
     |  
     |  SIGINT = <Signals.SIGINT: 2>
     |  
     |  SIGSEGV = <Signals.SIGSEGV: 11>
     |  
     |  SIGTERM = <Signals.SIGTERM: 15>
     |  
     |  SIG_DFL = <Handlers.SIG_DFL: 0>
     |  
     |  SIG_IGN = <Handlers.SIG_IGN: 1>
     |  
     |  Signals = <enum 'Signals'>
     |      An enumeration.
     |  
     |  __all__ = ['signal', 'getsignal']
     |  
     |  __extensions__ = ['signal', 'getsignal']
     |  
     |  __implements__ = []
     |  
     |  __imports__ = ['SIGBREAK', 'default_int_handler', '_signal', '_IntEnum...
     |  
     |  absolute_import = _Feature((2, 5, 0, 'alpha', 1), (3, 0, 0, 'alpha', 0...
     |  
     |  gevent = <module 'gevent' from 'D:\\Program Files\\Python35\\lib\\site...

FUNCTIONS
    get_hub(*args, **kwargs)
        Return the hub for the current thread.
        
        If a hub does not exist in the current thread, a new one is
        created of the type returned by :func:`get_hub_class`.
    
    getcurrent(...)
    
    idle(priority=0)
        Cause the calling greenlet to wait until the event loop is idle.
        
        Idle is defined as having no other events of the same or higher
        *priority* pending. That is, as long as sockets, timeouts or even
        signals of the same or higher priority are being processed, the loop
        is not idle.
        
        .. seealso:: :func:`sleep`
    
    iwait(objects, timeout=None, count=None)
        Iteratively yield *objects* as they are ready, until all (or *count*) are ready
        or *timeout* expired.
        
        :param objects: A sequence (supporting :func:`len`) containing objects
            implementing the wait protocol (rawlink() and unlink()).
        :keyword int count: If not `None`, then a number specifying the maximum number
            of objects to wait for. If ``None`` (the default), all objects
            are waited for.
        :keyword float timeout: If given, specifies a maximum number of seconds
            to wait. If the timeout expires before the desired waited-for objects
            are available, then this method returns immediately.
        
        .. seealso:: :func:`wait`
        
        .. versionchanged:: 1.1a1
           Add the *count* parameter.
        .. versionchanged:: 1.1a2
           No longer raise :exc:`LoopExit` if our caller switches greenlets
           in between items yielded by this function.
    
    kill(greenlet, exception=<class 'greenlet.GreenletExit'>)
        Kill greenlet asynchronously. The current greenlet is not unscheduled.
        
        .. note::
        
            The method :meth:`Greenlet.kill` method does the same and
            more (and the same caveats listed there apply here). However, the MAIN
            greenlet - the one that exists initially - does not have a
            ``kill()`` method, and neither do any created with :func:`spawn_raw`,
            so you have to use this function.
        
        .. caution:: Use care when killing greenlets. If they are not prepared for
           exceptions, this could result in corrupted state.
        
        .. versionchanged:: 1.1a2
            If the ``greenlet`` has a :meth:`kill <Greenlet.kill>` method, calls it. This prevents a
            greenlet from being switched to for the first time after it's been
            killed but not yet executed.
    
    killall(greenlets, exception=<class 'greenlet.GreenletExit'>, block=True, timeout=None)
        Forceably terminate all the ``greenlets`` by causing them to raise ``exception``.
        
        .. caution:: Use care when killing greenlets. If they are not prepared for exceptions,
           this could result in corrupted state.
        
        :param greenlets: A **bounded** iterable of the non-None greenlets to terminate.
           *All* the items in this iterable must be greenlets that belong to the same thread.
        :keyword exception: The exception to raise in the greenlets. By default this is
            :class:`GreenletExit`.
        :keyword bool block: If True (the default) then this function only returns when all the
            greenlets are dead; the current greenlet is unscheduled during that process.
            If greenlets ignore the initial exception raised in them,
            then they will be joined (with :func:`gevent.joinall`) and allowed to die naturally.
            If False, this function returns immediately and greenlets will raise
            the exception asynchronously.
        :keyword float timeout: A time in seconds to wait for greenlets to die. If given, it is
            only honored when ``block`` is True.
        :raise Timeout: If blocking and a timeout is given that elapses before
            all the greenlets are dead.
        
        .. versionchanged:: 1.1a2
            *greenlets* can be any iterable of greenlets, like an iterator or a set.
            Previously it had to be a list or tuple.
    
    reinit()
        Prepare the gevent hub to run in a new (forked) process.
        
        This should be called *immediately* after :func:`os.fork` in the
        child process. This is done automatically by
        :func:`gevent.os.fork` or if the :mod:`os` module has been
        monkey-patched. If this function is not called in a forked
        process, symptoms may include hanging of functions like
        :func:`socket.getaddrinfo`, and the hub's threadpool is unlikely
        to work.
        
        .. note:: Registered fork watchers may or may not run before
           this function (and thus ``gevent.os.fork``) return. If they have
           not run, they will run "soon", after an iteration of the event loop.
           You can force this by inserting a few small (but non-zero) calls to :func:`sleep`
           after fork returns. (As of gevent 1.1 and before, fork watchers will
           not have run, but this may change in the future.)
        
        .. note:: This function may be removed in a future major release
           if the fork process can be more smoothly managed.
        
        .. warning:: See remarks in :func:`gevent.os.fork` about greenlets
           and libev watchers in the child process.
    
    sleep(seconds=0, ref=True)
        Put the current greenlet to sleep for at least *seconds*.
        
        *seconds* may be specified as an integer, or a float if fractional
        seconds are desired.
        
        .. tip:: In the current implementation, a value of 0 (the default)
           means to yield execution to any other runnable greenlets, but
           this greenlet may be scheduled again before the event loop
           cycles (in an extreme case, a greenlet that repeatedly sleeps
           with 0 can prevent greenlets that are ready to do I/O from
           being scheduled for some (small) period of time); a value greater than
           0, on the other hand, will delay running this greenlet until
           the next iteration of the loop.
        
        If *ref* is False, the greenlet running ``sleep()`` will not prevent :func:`gevent.wait`
        from exiting.
        
        .. seealso:: :func:`idle`
    
    spawn(*args, **kwargs) method of builtins.type instance
        Create a new :class:`Greenlet` object and schedule it to run ``function(*args, **kwargs)``.
        This can be used as ``gevent.spawn`` or ``Greenlet.spawn``.
        
        The arguments are passed to :meth:`Greenlet.__init__`.
        
        .. versionchanged:: 1.1b1
            If a *function* is given that is not callable, immediately raise a :exc:`TypeError`
            instead of spawning a greenlet that will raise an uncaught TypeError.
    
    spawn_later(seconds, *args, **kwargs) method of builtins.type instance
        Create and return a new Greenlet object scheduled to run ``function(*args, **kwargs)``
        in the future loop iteration *seconds* later. This can be used as ``Greenlet.spawn_later``
        or ``gevent.spawn_later``.
        
        The arguments are passed to :meth:`Greenlet.__init__`.
        
        .. versionchanged:: 1.1b1
           If an argument that's meant to be a function (the first argument in *args*, or the ``run`` keyword )
           is given to this classmethod (and not a classmethod of a subclass),
           it is verified to be callable. Previously, the spawned greenlet would have failed
           when it started running.
    
    spawn_raw(function, *args, **kwargs)
        Create a new :class:`greenlet.greenlet` object and schedule it to
        run ``function(*args, **kwargs)``.
        
        This returns a raw :class:`~greenlet.greenlet` which does not have all the useful
        methods that :class:`gevent.Greenlet` has. Typically, applications
        should prefer :func:`~gevent.spawn`, but this method may
        occasionally be useful as an optimization if there are many
        greenlets involved.
        
        .. versionchanged:: 1.1b1
           If *function* is not callable, immediately raise a :exc:`TypeError`
           instead of spawning a greenlet that will raise an uncaught TypeError.
        
        .. versionchanged:: 1.1rc2
            Accept keyword arguments for ``function`` as previously (incorrectly)
            documented. Note that this may incur an additional expense.
        
        .. versionchanged:: 1.1a3
            Verify that ``function`` is callable, raising a TypeError if not. Previously,
            the spawned greenlet would have failed the first time it was switched to.
    
    wait(objects=None, timeout=None, count=None)
        Wait for ``objects`` to become ready or for event loop to finish.
        
        If ``objects`` is provided, it must be a list containing objects
        implementing the wait protocol (rawlink() and unlink() methods):
        
        - :class:`gevent.Greenlet` instance
        - :class:`gevent.event.Event` instance
        - :class:`gevent.lock.Semaphore` instance
        - :class:`gevent.subprocess.Popen` instance
        
        If ``objects`` is ``None`` (the default), ``wait()`` blocks until
        the current event loop has nothing to do (or until ``timeout`` passes):
        
        - all greenlets have finished
        - all servers were stopped
        - all event loop watchers were stopped.
        
        If ``count`` is ``None`` (the default), wait for all ``objects``
        to become ready.
        
        If ``count`` is a number, wait for (up to) ``count`` objects to become
        ready. (For example, if count is ``1`` then the function exits
        when any object in the list is ready).
        
        If ``timeout`` is provided, it specifies the maximum number of
        seconds ``wait()`` will block.
        
        Returns the list of ready objects, in the order in which they were
        ready.
        
        .. seealso:: :func:`iwait`
    
    with_timeout(seconds, function, *args, **kwds)
        Wrap a call to *function* with a timeout; if the called
        function fails to return before the timeout, cancel it and return a
        flag value, provided by *timeout_value* keyword argument.
        
        If timeout expires but *timeout_value* is not provided, raise :class:`Timeout`.
        
        Keyword argument *timeout_value* is not passed to *function*.

DATA
    __all__ = ['get_hub', 'Greenlet', 'GreenletExit', 'spawn', 'spawn_late...

VERSION
    1.2.2

FILE
    d:\program files\python35\lib\site-packages\gevent\__init__.py

"""