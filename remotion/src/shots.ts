import shotsJson from './shots.json';

export type Shot = {
  id: string;
  sec: number;
  window: string;
  en: string;
  zh: string;
  visual: string;
  emotion: string;
  motion: 'push-in' | 'pull-out' | 'drift-right' | 'hold';
  img_en: string;
  vid_en: string;
};

export type PovPackage = {
  channel_key: 'finance' | 'ai';
  channel_label: string;
  topic: string;
  topic_cn: string;
  duration: string;
  shot_count: number;
  word_count: number;
  shots: Shot[];
};

export const PACKAGES = shotsJson as unknown as PovPackage[];

export const getPackage = (key: 'finance' | 'ai'): PovPackage => {
  const found = PACKAGES.find((p) => p.channel_key === key);
  if (!found) throw new Error(`No package for channel: ${key}`);
  return found;
};

/** "1:12–1:25" | "0:00–0:10" -> [72, 85] （秒） */
export const parseWindow = (w: string): [number, number] => {
  const [a, b] = w.split(/[–—-]/).map((s) => s.trim());
  const toSec = (t: string) => {
    const [m, s] = t.split(':').map(Number);
    return m * 60 + (s || 0);
  };
  return [toSec(a), toSec(b)];
};

export const FPS = 30;
