// Service Worker for NutriTrack PWA
const CACHE_NAME = 'nutritrack-v1';
const urlsToCache = [
  '/',
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
      .catch(err => console.log('Cache install failed:', err))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
      .catch(err => fetch(event.request))
  );
});
