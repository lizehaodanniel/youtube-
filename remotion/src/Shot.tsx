import React, {Component, type ErrorInfo, type ReactNode} from 'react';
import {AbsoluteFill, Img, OffthreadVideo, interpolate, useCurrentFrame} from 'remotion';
import {getAsset} from './assets';
import type {Shot} from './shots';

/**
 * 单镜头。
 *
 * 设计原则（与 _build/pov_style.py 一致）：
 *  - 动效只有 4 种，每种只动一个轴。观众感知不到区别，但省掉 90% 返工。
 *  - 图里没有字 —— 字幕全部在这里用真字体叠加，随时可改、绝不出乱码。
 *  - 素材按 mp4 → png → svg 三级回退，任何一级缺失都会自动降级，
 *    所以「图还没生完」也能直接渲一条占位片看节奏。
 */

export const MOTION = {
  'push-in': {from: 1.0, to: 1.12, x: 0},
  'pull-out': {from: 1.12, to: 1.0, x: 0},
  'drift-right': {from: 1.06, to: 1.06, x: -60},
  hold: {from: 1.02, to: 1.05, x: 0},
} as const;

/* ---------------------------------------------------------- 安全兜底 */
class MediaBoundary extends Component<{fallback: ReactNode; children: ReactNode}, {failed: boolean}> {
  state = {failed: false};
  static getDerivedStateFromError() {
    return {failed: true};
  }
  componentDidCatch(_e: Error, _i: ErrorInfo) {
    this.setState({failed: true});
  }
  render() {
    return this.state.failed ? this.props.fallback : this.props.children;
  }
}

/* ---------------------------------------------------------- 占位块 */
const Placeholder: React.FC<{shot: Shot; channel: string}> = ({shot, channel}) => {
  const [a, b] = channel === 'finance' ? ['#16232B', '#E8A54B'] : ['#0B0E14', '#22D3EE'];
  return (
    <AbsoluteFill
      style={{
        background: `linear-gradient(135deg, ${a} 0%, ${b} 140%)`,
        alignItems: 'center',
        justifyContent: 'center',
        flexDirection: 'column',
        gap: 18,
      }}
    >
      <div style={{fontSize: 96, fontWeight: 800, color: 'rgba(255,255,255,.92)', letterSpacing: -2}}>
        {shot.id}
      </div>
      <div style={{fontSize: 28, color: 'rgba(255,255,255,.65)', maxWidth: '68%', textAlign: 'center', lineHeight: 1.5}}>
        {shot.visual}
      </div>
      <div style={{fontSize: 21, color: 'rgba(255,255,255,.38)', fontFamily: 'monospace'}}>
        public/{channel}/{shot.id}.png
      </div>
    </AbsoluteFill>
  );
};

/* ---------------------------------------------------------- 素材
 * 用构建期生成的清单，运行时不探测文件。
 * 原因：Remotion 的 <Img> / <OffthreadVideo> 遇到 404 会挂住 —— delayRender
 * 超时是在 React 渲染周期之外抛出的，错误边界接不住，整条渲染直接失败。
 */
const Media: React.FC<{shot: Shot; channel: 'finance' | 'ai'}> = ({shot, channel}) => {
  const asset = getAsset(shot.id);
  const style = {width: '100%', height: '100%', objectFit: 'cover'} as const;

  if (!asset) return <Placeholder shot={shot} channel={channel} />;

  return (
    <MediaBoundary fallback={<Placeholder shot={shot} channel={channel} />}>
      {asset.kind === 'mp4' ? <OffthreadVideo src={asset.src} style={style} /> : null}
      {asset.kind === 'png' || asset.kind === 'svg' ? <Img src={asset.src} style={style} /> : null}
    </MediaBoundary>
  );
};

/* ---------------------------------------------------------- 镜头 */
export const ShotView: React.FC<{
  shot: Shot;
  channel: 'finance' | 'ai';
  durationInFrames: number;
  fadeInFrames?: number;
}> = ({shot, channel, durationInFrames, fadeInFrames = 12}) => {
  const frame = useCurrentFrame();
  const m = MOTION[shot.motion] ?? MOTION.hold;

  const scale = interpolate(frame, [0, durationInFrames], [m.from, m.to], {
    extrapolateRight: 'clamp',
  });
  const translateX = interpolate(frame, [0, durationInFrames], [0, m.x], {
    extrapolateRight: 'clamp',
  });
  const opacity =
    fadeInFrames > 0 ? interpolate(frame, [0, fadeInFrames], [0, 1], {extrapolateRight: 'clamp'}) : 1;

  return (
    <AbsoluteFill style={{backgroundColor: '#000', opacity}}>
      <AbsoluteFill
        style={{transform: `scale(${scale}) translateX(${translateX}px)`, transformOrigin: 'center center'}}
      >
        <Media shot={shot} channel={channel} />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
