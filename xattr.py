import sys
import plistlib
import subprocess as sp
import argparse

PARSER = argparse.ArgumentParser(description='Script for setting attributes for multiple files in macOS')
PARSER.add_argument('--files', '-f', type=str, required=True, help='File paths, seperated by spaces')
PARSER.add_argument('--attrVals', '-a', type=str, required=True, help='Attribute values, seperated by ;')
PARSER.add_argument('--overwrite', '-o', action='store_true', help='Overwrite existing attributes')
#PARSER.add_argument('--attribute', '-a', type=str, help='xattr to modify')


XATTRS = {
	'tags': 'com.apple.metadata:_kMDItemUserTags'
}

attr = XATTRS['tags'] # TODO: cmdline argument
getCurPlistCmd = ['xattr', '-p', attr] # + [filepath]
setPlistCmd = ['xattr', '-w', attr] # + [plistString, filepath]



if __name__ == '__main__':

	args = PARSER.parse_args(sys.argv[1:])
	files = args.files.split(' ') # NOTE: will fail for paths with spaces
	newAttrs = args.attrVals.split(';') # TODO: $1. currently only works with array plist format

	for f in files:

		currentPlist = None
		updatedAttrs = None

		try:
			cmd = getCurPlistCmd + [f]
			currentPlist = sp.check_output(cmd)
		except sp.CalledProcessError: # no attributses found
			pass

		if currentPlist is None or args.overwrite == True:
			updatedAttrs = newAttrs
		else:
			prevAttrs = plistlib.readPlistFromString(currentPlist)
			updatedAttrs = newAttrs + prevAttrs # TODO: $1

		
		newPlist = plistlib.writePlistToString(updatedAttrs)
		cmd = setPlistCmd + [newPlist, f]
		sp.call(cmd)