#include <iostream>
#include <vector>
#include <algorithm>
// #include <string>

using namespace std;

class subset_enumerator_hadler
{
public:
    virtual bool check(const vector<int> &v, int n) = 0;
    virtual void back(const vector<int> &v, int n) = 0;
};

ostream &operator<<(ostream &out, const vector<int> &v)
{
    for (auto i : v)
        out << i << " ";
    return out;
}

class graph
{
private:
    vector<vector<int>> adjacency_lists;

public:
    graph(int n = 0)
        : adjacency_lists(n, vector<int>())
    {
    }

    const vector<int> &adjacency(int v) const
    {
        return adjacency_lists[v];
    }

    void add_edge(int u, int v)
    {
        if (find(adjacency_lists[u].begin(), adjacency_lists[u].end(), v) == adjacency_lists[u].end())
        {
            adjacency_lists[u].emplace_back(v);
            adjacency_lists[v].emplace_back(u);
        }
    }

    void remove_all_edges()
    {
        for (auto &a : adjacency_lists)
            a.clear();
    }

    int vertex_count() const
    {
        return adjacency_lists.size();
    }

    static graph from_graph6(const string &code)
    {
        graph g(code[0] - 63);
        int x = 0, y = 1;
        for (int i = 1, n = code.length(); i < n; ++i)
        {
            for (int j = 5; j >= 0; --j)
            {
                int bit = (code[i] - 63) >> j & 1;
                if (bit)
                    g.add_edge(x, y);
                if (++x == y)
                {
                    if (++y >= g.vertex_count())
                        return g;
                    x = 0;
                }
            }
        }
        return g;
    }

    ~graph() = default;
};

class domination_handler : public subset_enumerator_hadler
{
protected:
    const graph *g;
    vector<int> cover;
    int zeros;
    int upper_bound;

    inline void mark(int v)
    {
        if (cover[v]++ == 0)
        {
            zeros--;
        }
    }

    inline void unmark(int v)
    {
        if (--cover[v] == 0)
        {
            zeros++;
        }
    }

public:
    domination_handler(const graph &g)
        : g(&g), cover(g.vertex_count(), 0), zeros(g.vertex_count()), upper_bound(g.vertex_count())
    {
    }

    bool check(const vector<int> &v, int n) override
    {
        mark(v[n]);
        for (auto u : g->adjacency(v[n]))
        {
            mark(u);
        }
        if (zeros == 0)
        {
            upper_bound = n + 1;
        }
        if (n + 1 > upper_bound)
        {
            back(v, n);
            return false;
        }
        return true;
    }

    void back(const vector<int> &v, int n) override
    {
        unmark(v[n]);
        for (auto u : g->adjacency(v[n]))
        {
            unmark(u);
        }
    }

    int result() const
    {
        return upper_bound;
    }
};

class independence_handler : public domination_handler
{
public:
    independence_handler(const graph &g)
        : domination_handler(g)
    {
        upper_bound = 0;
    }
    bool check(const vector<int> &v, int n) override
    {
        // cout << "i \t" << cover<<" \t";
        // for (int i = 0; i < n; i++)
        // {
        //     cout << v[i] << " ";
        // }
        // cout << endl;
        if (cover[v[n]] != 0)
        {
            return false;
        }
        mark(v[n]);
        for (auto u : g->adjacency(v[n]))
        {
            mark(u);
        }
        if (zeros == 0 && n + 1 > upper_bound)
        {
            upper_bound = n + 1;
        }
        return true;
    }
};

ostream &operator<<(ostream &out, const graph &g)
{
    for (int i = 0; i < g.vertex_count(); ++i)
        out << i << "\t:\t" << g.adjacency(i) << "\n";
    return out;
}

// bool check_independent(const graph &g, const vector<int> &v, int n)
// {
//     for (int i = 0; i <= n; ++i)
//         cout << v[i] << " ";
//     cout << "+\n";
//     return true;
// }

void enumerate_subsets(subset_enumerator_hadler &h, int n, int k)
{
    auto subset = vector<int>(k);
    int level = -1;
    for (;;)
    {
        // cout << level << " || " << subset << endl;
        if (++level < k)
        {
            if (level == 0)
            {
                subset[level] = 0;
            }
            else
            {
                subset[level] = subset[level - 1] + 1;
            }
            if (subset[level] < n && h.check(subset, level))
            {
                continue;
            }
        }
        else
        {
            // cout << subset << endl;
            --level;
            h.back(subset, level);
        }

        while (level >= 0)
        {
            if (++subset[level] >= n)
            {
                if (--level >= 0)
                {
                    h.back(subset, level);
                }
            }
            else if (h.check(subset, level))
            {
                break;
            }
        }
        if (level < 0)
        {
            break;
        }
    }
}

int main(int argc, char **argv)
{
    string code;
    while (cin >> code)
    {
        graph g = graph::from_graph6(code);
        // cout << g;
        auto ih = independence_handler(g);
        auto dh = domination_handler(g);
        enumerate_subsets(ih, g.vertex_count(), g.vertex_count());
        enumerate_subsets(dh, g.vertex_count(), g.vertex_count());
        cout << code;
        cout << " \tindependence=" << ih.result();
        cout << " \tdomination=" << dh.result() << endl;
    }

    return 0;
}