import {Config} from '@remotion/cli/config';

Config.setVideoImageFormat('jpeg');
Config.setOverwriteOutput(true);
Config.setChromiumOpenGlRenderer('angle');
// 先跑一遍会很快：把并发数调到 CPU 核心数附近即可，再高不会更快
// Config.setConcurrency(8);
