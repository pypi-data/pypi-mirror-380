#ifndef metkit_version_h
#define metkit_version_h

#define metkit_VERSION_STR "1.15.1"
#define metkit_VERSION     "1.15.1"

#define metkit_VERSION_MAJOR 1
#define metkit_VERSION_MINOR 15
#define metkit_VERSION_PATCH 1

#define metkit_GIT_SHA1 "330b6f56de9d4c65cfa2bc03f3df62ddb4d76e7b"

#ifdef __cplusplus
extern "C" {
#endif

const char * metkit_version();

unsigned int metkit_version_int();

const char * metkit_version_str();

const char * metkit_git_sha1();

#ifdef __cplusplus
}
#endif


#endif // metkit_version_h
