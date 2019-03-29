from scripting_utils import *

def build(root_dir, android_submodule_dir, with_test_lib):
    # ------------------------------------------------------------------
    # Paths.
    src_dir        = '{0}/sdk/Adjust'.format(android_submodule_dir)
    jar_in_dir     = '{0}/sdk-core/build/libs'.format(src_dir)
    jar_out_dir    = '{0}/Assets/Adjust/Android'.format(root_dir)

    # ------------------------------------------------------------------
    # Building Android SDK JAR in release mode.
    debug_green('Building Android SDK JAR in release mode ...')
    change_dir(src_dir)
    gradle_make_sdk_jar_release()

    # ------------------------------------------------------------------
    # Copy Android SDK JAR to destination.
    debug_green('Copying generated Android SDK JAR to destination ...')
    copy_file('{0}/adjust-sdk-release.jar'.format(jar_in_dir), '{0}/adjust-android.jar'.format(jar_out_dir))

    if with_test_lib:
        # ------------------------------------------------------------------
        # Paths.
        set_log_tag('ANDROID-TEST-LIB-BUILD')
        debug_green('Building Test Library started ...')
        test_jar_in_dir  = '{0}/test-library/build/libs'.format(src_dir)
        test_jar_out_dir = '{0}/Assets/Adjust/Android/Test'.format(root_dir)

        # ------------------------------------------------------------------
        # Building Android test library JAR in debug mode.
        debug_green('Building Adjust test library JAR in debug mode ...')
        gradle_make_test_jar_debug()

        # ------------------------------------------------------------------
        # Copy Android test library JAR from to destination.
        debug_green('Copying generated Android test library JAR from {0} to {1} ...'.format(test_jar_in_dir, test_jar_out_dir))
        copy_file('{0}/test-library-debug.jar'.format(test_jar_in_dir), '{0}/adjust-test.jar'.format(test_jar_out_dir))