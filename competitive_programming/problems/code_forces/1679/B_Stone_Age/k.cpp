#include <bits/stdc++.h>

using namespace std;

template <typename A, typename B>
ostream &operator<<(ostream &os, const pair<A, B> &p) {
  return os << '(' << p.first << ", " << p.second << ')';
}
template <typename T_container, typename T = typename enable_if<
                                    !is_same<T_container, string>::value,
                                    typename T_container::value_type>::type>
ostream &operator<<(ostream &os, const T_container &v) {
  os << '{';
  string sep;
  for (const T &x : v)
    os << sep << x, sep = ", ";
  return os << '}';
}
void dbg_out() { cerr << endl; }
template <typename Head, typename... Tail> void dbg_out(Head H, Tail... T) {
  cerr << ' ' << H;
  dbg_out(T...);
}
#ifdef LOCAL
#define dbg(...) cerr << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)
#else
#define dbg(...)
#endif

#define ar array
#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

const int MAX_N = 1e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

const int N = 1e5; // limit for array size
int n;             // array size
int t[2 * N];
int h = sizeof(int) * 8 - __builtin_clz(n);
int d[N];

void calc(int p, int k) {
  if (d[p] == 0)
    t[p] = t[p << 1] + t[p << 1 | 1];
  else
    t[p] = d[p] * k;
}

void apply(int p, int value, int k) {
  t[p] = value * k;
  if (p < n)
    d[p] = value;
}

void build(int l, int r) {
  int k = 2;
  for (l += n, r += n - 1; l > 1; k <<= 1) {
    l >>= 1, r >>= 1;
    for (int i = r; i >= l; --i)
      calc(i, k);
  }
}

void push(int l, int r) {
  int s = h, k = 1 << (h - 1);
  for (l += n, r += n - 1; s > 0; --s, k >>= 1)
    for (int i = l >> s; i <= r >> s; ++i)
      if (d[i] != 0) {
        apply(i << 1, d[i], k);
        apply(i << 1 | 1, d[i], k);
        d[i] = 0;
      }
}

int query(int l, int r) {
  push(l, l + 1);
  push(r - 1, r);
  int res = 0;
  for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
    if (l & 1)
      res += t[l++];
    if (r & 1)
      res += t[--r];
  }
  return res;
}

void modify(int l, int r, int value) {
  if (value == 0)
    return;
  push(l, l + 1);
  push(r - 1, r);
  bool cl = false, cr = false;
  int k = 1;
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

  int tc = 1;
  int s = 1;
  cin >> tc >> n;
  h = sizeof(int) * 8 - __builtin_clz(n);

  for (int x = n; x > 0; x--) {
    cin >> v;
    modify(x, x + 1, v);
  }

  for (int t = 1; t <= tc; t++) {
    int type;
    int a;
    int b;

    cin >> type >> a;

    if (type == 1) {
      cin >> b;
      modify(a - 1, a, b);
    } else {
      modify(0, n, a);
    }

    cout << query(0, n) << "\n";
  }
}
