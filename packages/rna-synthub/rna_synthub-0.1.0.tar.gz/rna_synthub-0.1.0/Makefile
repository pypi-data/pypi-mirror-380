install_rnaqua:
	wget https://github.com/mantczak/rnaqua/releases/download/v1.1/rnaqua-binary.zip
	mkdir helper
	unzip rnaqua-binary.zip -d helper/rnaqua
	rm rnaqua-binary.zip
	chmod u+x helper/rnaqua/rnaqua-binary/bin/rnaqua.sh

install_cd_hit:
	mkdir -p lib/cd_hit
	git clone https://github.com/weizhongli/cdhit.git lib/cd_hit
	make -C lib/cd_hit

run_example:
	uv run synt_example

run_viz:
	uv run viz_cli