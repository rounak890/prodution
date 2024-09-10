.PHONY:= run check install runner # to tell that these dont correspond to filenames and even execute them if files with such filenames exsist so it works everytime
.DEFAULT_GOAL:=runner # else go for first one
run: install  # by defaukt executed since its first
	cd src; python runner.py # in one line bcoz we want to treat it as one not 2 seperate

install: pyproject.toml # check for the availabilty of 'pyproject.toml' file if exsisst the run else stop

clean: rm -rf `find . -type d -name __pycache__` # above is the bash cmd to remove all pycache folders

check:
	flake8 src/ # if flake8 tell any violations then it will stop execution

runner: check run clean # this is the pipeline which first do run then clean