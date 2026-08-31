import React from 'react';
import {AbsoluteFill, CalculateMetadataFunction, Sequence, staticFile} from 'remotion';
import {Caption} from './Caption';
import {ShotView} from './Shot';
import {FPS, PovPackage, getPackage, parseWindow} from './shots';

/**
 * 一条 POV 长片 = 一串镜头按时间轴排好，每个镜头盖一层字幕。
 *
 * 没有别的了。转场用交叉淡入（每个镜头开头 12 帧淡入），
 * 动效只有推/拉/平移/静止四种 —— 这是刻意保持的简单。
 */

export type PovProps = {
  channel: 'finance' | 'ai';
  captionLang: 'en' | 'zh' | 'both';
  fadeInFrames: number;
};

export const calcPovMetadata: CalculateMetadataFunction<PovProps> = ({props}) => {
  const pkg = getPackage(props.channel);
  const last = parseWindow(pkg.shots[pkg.shots.length - 1].window)[1];
  return {
    durationInFrames: Math.round(last * FPS) + FPS, // 结尾留 1 秒黑
    fps: FPS,
    width: 1920,
    height: 1080,
  };
};

export const PovVideo: React.FC<PovProps> = ({channel, captionLang, fadeInFrames}) => {
  const pkg: PovPackage = getPackage(channel);

  return (
    <AbsoluteFill style={{backgroundColor: '#000'}}>
      {pkg.shots.map((shot) => {
        const [start, end] = parseWindow(shot.window);
        const from = Math.round(start * FPS);
        const dur = Math.max(1, Math.round((end - start) * FPS));
        return (
          <Sequence key={shot.id} from={from} durationInFrames={dur} name={shot.id}>
            <ShotView
              shot={shot}
              channel={channel}
              durationInFrames={dur}
              fadeInFrames={fadeInFrames}
            />
            <Caption
              text={shot.en}
              sub={shot.zh}
              durationInFrames={dur}
              lang={captionLang}
            />
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};

/** 每个频道注册成一个 composition，这样渲染命令里不用带 props */
export const makeComposition = (channel: 'finance' | 'ai') => ({
  component: PovVideo,
  id: channel === 'finance' ? 'PovVideoFinance' : 'PovVideoAi',
  defaultProps: {channel, captionLang: 'en' as const, fadeInFrames: 12},
  calculateMetadata: calcPovMetadata,
});

/** 供自检脚本用：列出缺失的素材 */
export const missingAssets = (channel: 'finance' | 'ai'): string[] => {
  const pkg = getPackage(channel);
  const out: string[] = [];
  for (const s of pkg.shots) {
    try {
      staticFile(`${channel}/${s.id}.png`);
    } catch {
      out.push(`${channel}/${s.id}.png`);
    }
  }
  return out;
};
