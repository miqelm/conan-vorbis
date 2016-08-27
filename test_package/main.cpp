#include "vorbis/codec.h"
#include <iostream>

using namespace std;

int main (void){
	
	vorbis_info vi;
	vorbis_info_init(&vi);
	cout << "Vorbis version: " << vi.version << endl;
  
}
