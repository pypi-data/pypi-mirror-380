import click

from rnadvisor.rnadvisor_cli import RNAdvisorCLI

class SFModels:
    def __init__(self, score: str, in_dir: str, out_path: str, out_time_path: str):
        self.score = score if isinstance(score, list) else [score]
        self.in_dir = in_dir
        self.out_path = out_path
        self.out_time_path = out_time_path

    def run(self):
        rnadvisor_cli = RNAdvisorCLI(
            pred_dir=self.in_dir,
            native_path=None,
            out_path=self.out_path,
            scores = self.score,
            out_time_path = self.out_time_path,
            z_score=True,
        )
        rnadvisor_cli.predict()

@click.command()
@click.option( "--score", type=str, help="Score to compute", )
@click.option("--in_dir", type=str, default=None, help="Input directory containing RNA models")
@click.option("--out_path", type=str, default=None, help="Output CSV file path to save the scores")
@click.option("--out_time_path", type=str, default=None, help="Output path to save the computation time")
def main(score: str, in_dir, out_path, out_time_path):
    sf_models = SFModels(score, in_dir, out_path, out_time_path)
    sf_models.run()

if __name__ == "__main__":
    main()