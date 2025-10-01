from pathlib import Path
import sys
from typing import Generator

from _test_utils import\
	INIT_SYS_PATH,\
	TEST_DIR,\
	REPO_ROOT,\
	LIB_DIR,\
	assert_path_in_sys_path,\
	assert_path_is_present,\
	reset_sys_path

sys.path.insert(0, str(REPO_ROOT))
from syspathmodif import SysPathBundle
reset_sys_path()


def _generate_paths() -> Generator[Path, None, None]:
	yield TEST_DIR
	yield REPO_ROOT
	yield LIB_DIR


def test_init_generator() -> None:
	try:
		from inspect import isgenerator

		content_gen = _generate_paths()
		assert isgenerator(content_gen)
		bundle = SysPathBundle(content_gen)
		assert not bundle.cleared_on_del

		assert_path_is_present(TEST_DIR, bundle, True, False)
		assert_path_is_present(REPO_ROOT, bundle, True, True)
		assert_path_is_present(LIB_DIR, bundle, True, True)

	finally:
		reset_sys_path()


def test_init_list() -> None:
	try:
		content = [TEST_DIR, REPO_ROOT, LIB_DIR]
		assert isinstance(content, list)
		bundle = SysPathBundle(content)
		assert not bundle.cleared_on_del

		assert_path_is_present(TEST_DIR, bundle, True, False)
		assert_path_is_present(REPO_ROOT, bundle, True, True)
		assert_path_is_present(LIB_DIR, bundle, True, True)

	finally:
		reset_sys_path()


def test_init_tuple() -> None:
	try:
		content = (TEST_DIR, REPO_ROOT, LIB_DIR)
		assert isinstance(content, tuple)
		bundle = SysPathBundle(content)
		assert not bundle.cleared_on_del

		assert_path_is_present(TEST_DIR, bundle, True, False)
		assert_path_is_present(REPO_ROOT, bundle, True, True)
		assert_path_is_present(LIB_DIR, bundle, True, True)

	finally:
		reset_sys_path()


def test_init_set() -> None:
	try:
		content = {TEST_DIR, REPO_ROOT, LIB_DIR}
		assert isinstance(content, set)
		bundle = SysPathBundle(content)
		assert not bundle.cleared_on_del

		assert_path_is_present(TEST_DIR, bundle, True, False)
		assert_path_is_present(REPO_ROOT, bundle, True, True)
		assert_path_is_present(LIB_DIR, bundle, True, True)

	finally:
		reset_sys_path()


def test_clear() -> None:
	try:
		bundle = SysPathBundle((TEST_DIR, REPO_ROOT, LIB_DIR))
		bundle.clear()

		assert_path_is_present(TEST_DIR, bundle, True, False)
		assert_path_is_present(REPO_ROOT, bundle, False, False)
		assert_path_is_present(LIB_DIR, bundle, False, False)

		assert sys.path == INIT_SYS_PATH

	finally:
		reset_sys_path()


def test_cleared_on_del() -> None:
	try:
		bundle = SysPathBundle((TEST_DIR, REPO_ROOT, LIB_DIR), True)
		assert bundle.cleared_on_del
		del bundle

		assert_path_in_sys_path(TEST_DIR, True)
		assert_path_in_sys_path(REPO_ROOT, False)
		assert_path_in_sys_path(LIB_DIR, False)

		assert sys.path == INIT_SYS_PATH

	finally:
		reset_sys_path()


def test_context_management() -> None:
	try:
		with SysPathBundle((TEST_DIR, REPO_ROOT, LIB_DIR)) as bundle:
			assert_path_is_present(TEST_DIR, bundle, True, False)
			assert_path_is_present(REPO_ROOT, bundle, True, True)
			assert_path_is_present(LIB_DIR, bundle, True, True)

		assert_path_in_sys_path(TEST_DIR, True)
		assert_path_in_sys_path(REPO_ROOT, False)
		assert_path_in_sys_path(LIB_DIR, False)

		assert sys.path == INIT_SYS_PATH

	finally:
		reset_sys_path()
