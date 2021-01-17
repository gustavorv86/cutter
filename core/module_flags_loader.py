
import core.module_flags.filter
import core.module_flags.format
import core.module_flags.nfilter
import core.module_flags.columns
import core.module_flags.search_and_replace
import core.module_flags.substring


def get_modules():

	flag_methods = dict()

	flag_methods[core.module_flags.filter.NAME] = core.module_flags.filter
	flag_methods[core.module_flags.format.NAME] = core.module_flags.format
	flag_methods[core.module_flags.nfilter.NAME] = core.module_flags.nfilter
	flag_methods[core.module_flags.columns.NAME] = core.module_flags.columns
	flag_methods[core.module_flags.search_and_replace.NAME] = core.module_flags.search_and_replace
	flag_methods[core.module_flags.substring.NAME] = core.module_flags.substring

	return flag_methods
