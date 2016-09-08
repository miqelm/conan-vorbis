#include "vorbis/codec.h"
#include <stdio.h>

int main (void){
	
	vorbis_info vi;
	vorbis_info_init(&vi);
	printf("Version variable in initialised vorbis info struct: %d\n\r", vi.version);
  
}
