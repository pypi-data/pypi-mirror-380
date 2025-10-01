#ifndef _attribute_h_INCLUDED
#define _attribute_h_INCLUDED

#ifndef _MSC_VER
#define ATTRIBUTE_FORMAT(FORMAT_POSITION, VARIADIC_ARGUMENT_POSITION) \
  __attribute__ (( \
      format (printf, FORMAT_POSITION, VARIADIC_ARGUMENT_POSITION)))
#else
#define ATTRIBUTE_FORMAT(FORMAT_POSITION, VARIADIC_ARGUMENT_POSITION) // ignore on MSVC
#endif

#ifndef _MSC_VER
#define ATTRIBUTE_ALWAYS_INLINE __attribute__ ((always_inline))
#else
#define ATTRIBUTE_ALWAYS_INLINE // ignore on MSVC
#endif

#endif
