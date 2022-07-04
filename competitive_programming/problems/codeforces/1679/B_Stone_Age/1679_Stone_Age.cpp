#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define ld long double

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

const int N = 1e5; // limit for array size
int n;             // array size
int t[2 * N];
int h = sizeof(int) * 8 - __builtin_clz(n);
int d[N];

void calc(ll p, ll k) {
  if (d[p] == 0)
    t[p] = t[p << 1] + t[p << 1 | 1];
  else
    t[p] = d[p] * k;
}

void apply(ll p, ll value, ll k) {
  t[p] = value * k;
  if (p < n)
    d[p] = value;
}

void build(ll l, ll r) {
  ll k = 2;
  for (l += n, r += n - 1; l > 1; k <<= 1) {
    l >>= 1, r >>= 1;
    for (ll i = r; i >= l; --i)
      calc(i, k);
  }
}

void push(ll l, ll r) {
  ll s = h, k = 1 << (h - 1);
  for (l += n, r += n - 1; s > 0; --s, k >>= 1)
    for (ll i = l >> s; i <= r >> s; ++i)
      if (d[i] != 0) {
        apply(i << 1, d[i], k);
        apply(i << 1 | 1, d[i], k);
        d[i] = 0;
      }
}

ll query(ll l, ll r) {
  push(l, l + 1);
  push(r - 1, r);
  ll res = 0;
  for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
    if (l & 1)
      res += t[l++];
    if (r & 1)
      res += t[--r];
  }
  return res;
}

void modify(ll l, ll r, ll value) {
  if (value == 0)
    return;
  push(l, l + 1);
  push(r - 1, r);
  bool cl = false, cr = false;
  ll k = 1;
  for (l += n, r += n; l < r; l >>= 1, r >>= 1, k <<= 1) {
    if (cl)
      calc(l - 1, k);
    if (cr)
      calc(r, k);
    if (l & 1)
      apply(l++, value, k), cl = true;
    if (r & 1)
      apply(--r, value, k), cr = true;
  }
  for (--l; r > 0; l >>= 1, r >>= 1, k <<= 1) {
    if (cl)
      calc(l, k);
    if (cr && (!cl || l != r))
      calc(r, k);
  }
}

int main() {
  ll l, r, v;

  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  ll tc = 1;
  ll s = 1;
  cin >> tc >> n;

  for (ll x = n; x > 0; x--) {
    cin >> v;
    modify(x, x + 1, v);
  }

  for (ll ct = 1; ct <= tc; ct++) {
    ll type;
    ll a;
    ll b;
    ll res;

    cin >> type >> a;

    if (type == 1) {
      cin >> b;
      modify(a - 1, a, b);
      res = query(0, n);
    } else {
      modify(0, n, a);
      res = n * a;
    }

    cout << res << "\n";
  }
}
