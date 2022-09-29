#include "./Dependencies/Crypto++/cryptlib.h"
#include "./Dependencies/Crypto++/base64.h"
#include "./Dependencies/Crypto++/hex.h"
#include "./Dependencies/Crypto++/rsa.h"
#include "./Dependencies/Crypto++/aes.h"
#include "./Dependencies/Crypto++/files.h"
#include "./Dependencies/Crypto++/randpool.h"
#include "./Dependencies/Crypto++/validate.h"
// #include "./Dependencies/Crypto++/modes.h"
// #include "./Dependencies/Crypto++/osrng.h"
// #include "./Dependencies/Crypto++/seckey.h"

#include <iostream>

int main() {
    std::cout << "love" << std::endl;
}
// int main(int argc, char* argv[]) {
//     using namespace CryptoPP;

//     unsigned char *key = (unsigned char *)"01234567890123456789012345678901";
//     unsigned char *iv = (unsigned char *)"0123456789012345";
//     size_t key_size = strlen((const char*)key);

//     if (argc != 3) {
//         fprintf(stdout, "Usage  : %s <encrypt file> <decrypt file>\n", argv[0]);
//         fprintf(stdout, "Example : %s my_encrypt_msg.txt my_decrypt_msg.txt\n", argv[0]);
//         exit(EXIT_FAILURE);
//     }

//     CBC_Mode<AES>::Decryption       decryptor(key, key_size, iv);
//     std::cout << "Algorithm Name: " << decryptor.AlgorithmName() << std::endl;
//     std::cout << "Default Key Length: " << decryptor.DefaultKeyLength() << std::endl;
//     std::cout << "Key Size: " << key_size << std::endl;
//     std::cout << "Maximum Key Length: " << decryptor.MaxKeyLength() << std::endl;
//     std::cout << "Minimum Key Length: " << decryptor.MinKeyLength() << std::endl;
//     std::cout << "IV size: " << decryptor.IVSize() << std::endl;
//     std::cout << "Maximum IV Length: " << decryptor.MaxIVLength() << std::endl;
//     std::cout << "Minimum IV Length: " << decryptor.MinIVLength() << std::endl;

//     FileSource(argv[1], true, new StreamTransformationFilter(decryptor, new FileSink(argv[2])));


//     return 0;
// }
