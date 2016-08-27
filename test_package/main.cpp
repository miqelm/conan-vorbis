#include "vorbis/codec.h"
#include <iostream>

using namespace std;

int main (void){
	
	vorbis_info vi;
	vorbis_info_init(&vi);
	cout << "Version variable in initialised vorbis info struct: " << vi.version << endl;
  
}
