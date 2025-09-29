#ifndef _handle_h_INCLUDED
#define _handle_h_INCLUDED

#include <signal.h>

void kissat_init_signal_handler (void (*handler) (int));
void kissat_reset_signal_handler (void);

void kissat_init_alarm (void (*handler) (void));
void kissat_reset_alarm (void);

#if defined(__MINGW32__) || defined(_MSC_VER)
#define SIGNAL_SIGBUS
#else
#define SIGNAL_SIGBUS SIGNAL (SIGBUS)
#endif

#define SIGNALS \
  SIGNAL (SIGABRT) \
  SIGNAL_SIGBUS \
  SIGNAL (SIGINT) \
  SIGNAL (SIGSEGV) \
  SIGNAL (SIGTERM)

// clang-format off

static inline const char *
kissat_signal_name (int sig)
{
#define SIGNAL(SIG) \
  if (sig == SIG) return #SIG;
  SIGNALS
#undef SIGNAL
#if !defined(__MINGW32__) && !defined(_MSC_VER)
  if (sig == SIGALRM)
    return "SIGALRM";
#endif
  return "SIGUNKNOWN";
}

// clang-format on

#endif
