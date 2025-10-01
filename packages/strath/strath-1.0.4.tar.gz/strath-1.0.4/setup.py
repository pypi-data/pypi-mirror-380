import setuptools


_ENCODING_UTF8 = "utf-8"
_MODE_R = "r"

_NEW_LINE = "\n"


def _make_descriptions():
	with open("README.md", _MODE_R, encoding=_ENCODING_UTF8) as readme_file:
		readme_content = readme_file.read()

	title_fr = "## FRANÇAIS"
	title_en = "## ENGLISH"

	index_title_fr = readme_content.index(title_fr)
	index_demos_fr = readme_content.index("### Démos")

	index_title_en = readme_content.index(title_en)
	index_desc_en = index_title_en + len(title_en)
	index_desc_end_en = readme_content.index("In Python", index_desc_en)
	index_demos_en = readme_content.index("### Demos", index_title_en)

	short_description = readme_content[index_desc_en: index_desc_end_en]
	short_description = short_description.strip()
	short_description = short_description.replace(_NEW_LINE, " ")
	short_description = short_description.replace("`", "")

	long_description = readme_content[index_title_fr: index_demos_fr]\
		+ readme_content[index_title_en:index_demos_en].rstrip()

	return short_description, long_description


if __name__ == "__main__":
	short_desc, long_desc = _make_descriptions()

	setuptools.setup(
		name = "strath",
		version = "1.0.4",
		author = "Guyllaume Rousseau",
		description = short_desc,
		long_description = long_desc,
		long_description_content_type = "text/markdown",
		url = "https://github.com/GRV96/strath",
		classifiers = [
			"Development Status :: 5 - Production/Stable",
			"Intended Audience :: Developers",
			"License :: OSI Approved :: MIT License",
			"Operating System :: OS Independent",
			"Programming Language :: Python :: 3.10",
			"Topic :: Utilities"
		],
		packages = setuptools.find_packages(
			exclude=(".github", "demos", "tests")),
		license = "MIT",
		license_files = ("LICENSE",))
