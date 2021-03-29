#include <pybind11/pybind11.h>
#include <aesni.h>
namespace py = pybind11;

unsigned char* encrypt(const unsigned char key[], unsigned char msg[AES128_BLOCKLEN]){
    
    
}


PYBIND11_MODULE(example, m) {
    m.doc() = "libs cc plugs";

    m.def("encrypt", [](const unsigned char key[], unsigned char msg[AES128_BLOCKLEN]){
        struct aes128 ctx;
        aes128_init(&ctx, key);
        unsigned char ct[AES128_BLOCKLEN] = {0};
        aes128_encrypt(&ctx, &ct, msg);
        return ct;

    });
}