import React from 'react';
import {Composition} from 'remotion';
import {makeComposition} from './PovVideo';

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition {...makeComposition('finance')} width={1920} height={1080} fps={30} durationInFrames={21000} />
      <Composition {...makeComposition('ai')} width={1920} height={1080} fps={30} durationInFrames={17400} />
    </>
  );
};
