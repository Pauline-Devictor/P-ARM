#include "parm.h"

BEGIN();
END();

void run()
{
  BEGIN();
  int a = 1;
  int b = 2;
  int c = a+b;
  RES = c;
  END();
}

END();
BEGIN();