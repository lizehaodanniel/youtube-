import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';

/**
 * 字幕。字幕是后期叠加的，不是烧在图里的 —— 所以永远不会出现 AI 渲染的乱码字符，
 * 而且你随时能改文案而不用重生图。
 */

export const Caption: React.FC<{
  text: string;
  sub?: string;
  durationInFrames: number;
  fade?: number;
  lang?: 'en' | 'zh' | 'both';
}> = ({text, sub, durationInFrames, fade = 8, lang = 'en'}) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(
    frame,
    [0, fade, durationInFrames - fade, durationInFrames],
    [0, 1, 1, 0.92],
    {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}
  );
  const rise = interpolate(frame, [0, fade], [14, 0], {extrapolateRight: 'clamp'});

  const showEn = lang === 'en' || lang === 'both';
  const showZh = lang === 'zh' || lang === 'both';

  return (
    <AbsoluteFill
      style={{
        justifyContent: 'flex-end',
        alignItems: 'center',
        paddingBottom: lang === 'both' ? 78 : 96,
        paddingLeft: 90,
        paddingRight: 90,
      }}
    >
      {/* 底部压暗，保证白字在亮画面上也读得清 */}
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          bottom: 0,
          height: 340,
          background: 'linear-gradient(to top, rgba(0,0,0,.72) 0%, rgba(0,0,0,.35) 45%, rgba(0,0,0,0) 100%)',
        }}
      />
      <div
        style={{
          opacity,
          transform: `translateY(${rise}px)`,
          textAlign: 'center',
          maxWidth: 1560,
        }}
      >
        {showEn ? (
          <div
            style={{
              fontFamily: 'Inter, "Helvetica Neue", Arial, sans-serif',
              fontSize: lang === 'both' ? 46 : 54,
              fontWeight: 700,
              lineHeight: 1.28,
              color: '#FFFFFF',
              textShadow: '0 3px 0 rgba(0,0,0,.55), 0 0 22px rgba(0,0,0,.75), 0 6px 26px rgba(0,0,0,.6)',
              letterSpacing: 0.2,
            }}
          >
            {text}
          </div>
        ) : null}
        {showZh ? (
          <div
            style={{
              fontFamily: '"PingFang SC", "Microsoft YaHei", sans-serif',
              fontSize: lang === 'both' ? 30 : 46,
              fontWeight: 600,
              lineHeight: 1.4,
              color: 'rgba(255,255,255,.88)',
              marginTop: lang === 'both' ? 12 : 0,
              textShadow: '0 2px 0 rgba(0,0,0,.5), 0 0 18px rgba(0,0,0,.7)',
            }}
          >
            {sub ?? text}
          </div>
        ) : null}
      </div>
    </AbsoluteFill>
  );
};
