import { exec } from 'child_process';

const Pipeline = class Pipeline {
  constructor(app) {
    this.app = app;
    this.run();
  }

  run() {
    this.app.get('/pipeline', (req, res) => {
      exec('python3 ./src/controllers/user.py', (error, stdout) => {
        if (error) {
          console.error(`[ERROR] pipeline -> ${error}`);
          res.status(500).json({
            code: 500,
            message: 'Internal Server error'
          });
          return;
        }
        try {
          const jsonOutput = JSON.parse(stdout);
          res.status(200).json(jsonOutput);
        } catch (e) {
          console.error(`[ERROR] pipeline -> ${e}`);
          res.status(500).json({
            code: 500,
            message: 'Error parsing JSON output'
          });
        }
      });
    });
  }
};

export default Pipeline;
