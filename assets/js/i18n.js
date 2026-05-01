/* ============================================================
 * i18n.js — client-side bilingual (EN / KO) support
 *
 * What it does:
 *   1. Auto-redirect from "/" to /en/ or /ko/ based on cookie or
 *      browser language (one-time per session).
 *   2. Inject a floating language toggle in the top-right corner
 *      of every localised page; clicking it goes to the matching
 *      slug in the other language.
 *   3. Tag sidebar nav items with data-nav-lang so the CSS in
 *      i18n.css can hide the opposite-language tree.
 * ============================================================ */

(function () {
  'use strict';

  var COOKIE = 'rh_lang';
  var REDIRECT_FLAG = 'rh_redirected';
  var BASE_PATH = computeBasePath();

  function computeBasePath() {
    var p = window.location.pathname;
    // If we're at a localised page, base = everything before /en/ or /ko/.
    var langMatch = p.match(/^(.*?)\/(en|ko)(?:\/|$)/);
    if (langMatch) return langMatch[1] || '';
    // Otherwise, infer from project-site pattern: /<repo>/ as the only segment.
    var parts = p.split('/').filter(Boolean);
    if (parts.length === 0) return '';
    if (parts.length === 1) return '/' + parts[0];
    // Also handle .../index.html on a project root.
    if (parts[parts.length - 1] === 'index.html' && parts.length === 2) {
      return '/' + parts[0];
    }
    return '';
  }

  function getCookie(name) {
    return document.cookie.split('; ').reduce(function (acc, pair) {
      var idx = pair.indexOf('=');
      var k = idx > -1 ? pair.substring(0, idx) : pair;
      var v = idx > -1 ? pair.substring(idx + 1) : '';
      return k === name ? v : acc;
    }, null);
  }

  function setCookie(name, value, days) {
    var maxAge = (days || 365) * 24 * 60 * 60;
    document.cookie = name + '=' + encodeURIComponent(value) +
      '; path=/; max-age=' + maxAge + '; SameSite=Lax';
  }

  function detectPageLang() {
    var m = window.location.pathname.match(/\/(en|ko)(?:\/|$)/);
    return m ? m[1] : null;
  }

  function isRootPath() {
    var p = window.location.pathname;
    if (p === '/') return true;
    if (BASE_PATH && (p === BASE_PATH || p === BASE_PATH + '/')) return true;
    if (p.endsWith('/index.html')) return true;
    return false;
  }

  /* ---------- 1. Auto-redirect on root ---------- */
  function maybeRedirect() {
    if (!isRootPath()) return;
    if (sessionStorage.getItem(REDIRECT_FLAG)) return;

    var saved = getCookie(COOKIE);
    var browser = (navigator.language || navigator.userLanguage || 'en').toLowerCase();
    var target = saved || (browser.indexOf('ko') === 0 ? 'ko' : 'en');

    sessionStorage.setItem(REDIRECT_FLAG, '1');
    var dest = (BASE_PATH || '') + '/' + target + '/';
    // Avoid an infinite loop if BASE_PATH detection failed.
    if (window.location.pathname === dest) return;
    window.location.replace(dest);
  }

  /* ---------- 2. Floating language toggle ---------- */
  function injectToggle(pageLang) {
    if (!pageLang) return;
    if (document.getElementById('lang-toggle')) return;

    var other = pageLang === 'en' ? 'ko' : 'en';
    var here = window.location.pathname;
    var there = here.replace('/' + pageLang + '/', '/' + other + '/');

    var box = document.createElement('div');
    box.id = 'lang-toggle';
    box.setAttribute('role', 'navigation');
    box.setAttribute('aria-label', 'Language switcher');

    var current = document.createElement('span');
    current.className = 'lang-current';
    current.textContent = pageLang === 'en' ? 'EN' : '한국어';
    box.appendChild(current);

    var sep = document.createElement('span');
    sep.className = 'lang-sep';
    sep.setAttribute('aria-hidden', 'true');
    sep.textContent = '·';
    box.appendChild(sep);

    var link = document.createElement('a');
    link.href = there;
    link.className = 'lang-switch';
    link.setAttribute('data-lang-switch', other);
    link.textContent = other === 'ko' ? '한국어' : 'English';
    link.addEventListener('click', function () {
      setCookie(COOKIE, other);
    });
    box.appendChild(link);

    document.body.appendChild(box);
  }

  /* ---------- 3. Tag sidebar items per language ---------- */
  function tagSidebar() {
    var links = document.querySelectorAll('.nav-list-item .nav-list-link, .site-nav .nav-list-link');
    Array.prototype.forEach.call(links, function (link) {
      var href = link.getAttribute('href') || '';
      var item = link.closest('.nav-list-item');
      if (!item || item.hasAttribute('data-nav-lang')) return;
      if (/\/en(\/|$)/.test(href)) item.setAttribute('data-nav-lang', 'en');
      else if (/\/ko(\/|$)/.test(href)) item.setAttribute('data-nav-lang', 'ko');
    });
  }

  /* ---------- bootstrap ---------- */
  maybeRedirect();

  function onReady(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }

  onReady(function () {
    var lang = detectPageLang();
    if (lang) {
      setCookie(COOKIE, lang);
      injectToggle(lang);
    }
    tagSidebar();
    // Re-tag on dynamic sidebar updates (just-the-docs sometimes lazy-renders).
    var observer = new MutationObserver(tagSidebar);
    var nav = document.querySelector('.site-nav, nav.site-nav, .main-nav');
    if (nav) observer.observe(nav, { childList: true, subtree: true });
  });
})();
