import pytest

import sys

from _test_utils import\
	INIT_SYS_PATH,\
	TEST_DIR,\
	REPO_ROOT,\
	LIB_DIR,\
	assert_path_in_sys_path,\
	index_in_sys_path,\
	reset_sys_path

sys.path.insert(0, str(REPO_ROOT))
from syspathmodif import\
	sp_append,\
	sp_contains,\
	sp_prepend,\
	sp_remove
reset_sys_path()


_PATH_TYPE_ERROR_MSG = "The path must be None or of type str or pathlib.Path."


def test_sp_contains_true_str() -> None:
	# This test does not change the content of sys.path.
	assert sp_contains(str(TEST_DIR))


def test_sp_contains_true_pathlib() -> None:
	# This test does not change the content of sys.path.
	assert sp_contains(TEST_DIR)


def test_sp_contains_false_str() -> None:
	# This test does not change the content of sys.path.
	assert not sp_contains(str(LIB_DIR))


def test_sp_contains_false_pathlib() -> None:
	# This test does not change the content of sys.path.
	assert not sp_contains(LIB_DIR)


def test_sp_contains_none() -> None:
	# This test does not change the content of sys.path.
	assert not sp_contains(None)


def test_sp_contains_exception() -> None:
	# This test does not change the content of sys.path.
	with pytest.raises(TypeError, match=_PATH_TYPE_ERROR_MSG):
		sp_contains(3.14159)


def test_sp_prepend_str() -> None:
	try:
		lib_dir = str(LIB_DIR)
		success = sp_prepend(lib_dir)
		assert success
		assert index_in_sys_path(lib_dir) == 0
	finally:
		reset_sys_path()


def test_sp_prepend_pathlib() -> None:
	try:
		success = sp_prepend(LIB_DIR)
		assert success
		assert index_in_sys_path(LIB_DIR) == 0
	finally:
		reset_sys_path()


def test_sp_prepend_no_success() -> None:
	try:
		sys.path.append(str(LIB_DIR))
		success = sp_prepend(LIB_DIR)
		assert not success
		assert_path_in_sys_path(LIB_DIR, True)
	finally:
		reset_sys_path()


def test_sp_prepend_none() -> None:
	try:
		success = sp_prepend(None)
		assert not success
		assert sys.path == INIT_SYS_PATH
	finally:
		reset_sys_path()


def test_sp_append_str() -> None:
	try:
		lib_dir = str(LIB_DIR)
		success = sp_append(lib_dir)
		assert success
		assert index_in_sys_path(lib_dir) == len(sys.path) - 1
	finally:
		reset_sys_path()


def test_sp_append_pathlib() -> None:
	try:
		success = sp_append(LIB_DIR)
		assert success
		assert index_in_sys_path(LIB_DIR) == len(sys.path) - 1
	finally:
		reset_sys_path()


def test_sp_append_no_success() -> None:
	try:
		sys.path.append(str(LIB_DIR))
		success = sp_append(LIB_DIR)
		assert not success
		assert_path_in_sys_path(LIB_DIR, True)
	finally:
		reset_sys_path()


def test_sp_append_none() -> None:
	try:
		success = sp_append(None)
		assert not success
		assert sys.path == INIT_SYS_PATH
	finally:
		reset_sys_path()


def test_sp_remove_str() -> None:
	try:
		sys.path.append(str(LIB_DIR))
		success = sp_remove(str(LIB_DIR))
		assert success
		assert_path_in_sys_path(LIB_DIR, False)
	finally:
		reset_sys_path()


def test_sp_remove_pathlib() -> None:
	try:
		sys.path.append(str(LIB_DIR))
		success = sp_remove(LIB_DIR)
		assert success
		assert_path_in_sys_path(LIB_DIR, False)
	finally:
		reset_sys_path()


def test_sp_remove_no_success() -> None:
	try:
		# sys.path does not contain LIB_DIR.
		success = sp_remove(LIB_DIR)
		assert not success
		assert_path_in_sys_path(LIB_DIR, False)
	finally:
		reset_sys_path()


def test_sp_remove_none_no_success() -> None:
	try:
		success = sp_remove(None)
		assert not success
		assert sys.path == INIT_SYS_PATH
	finally:
		reset_sys_path()


def test_sp_remove_none_success() -> None:
	try:
		sys.path.append(None)
		success = sp_remove(None)
		assert success
		assert sys.path == INIT_SYS_PATH
	finally:
		reset_sys_path()
