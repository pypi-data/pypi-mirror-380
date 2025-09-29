import { defineComponent as p, useAttrs as d, useSlots as C, createBlock as h, openBlock as g, mergeProps as S, unref as i, createSlots as v, renderList as D, withCtx as b, renderSlot as y, normalizeProps as A, guardReactiveProps as x, computed as f, ref as $, watch as T, resolveDynamicComponent as k } from "vue";
import * as _ from "tdesign-vue-next";
function I(n) {
  const { container: t = ".insta-main" } = n;
  return t;
}
const B = /* @__PURE__ */ p({
  inheritAttrs: !1,
  __name: "Affix",
  setup(n) {
    const t = d(), r = C(), o = I(t);
    return (e, s) => (g(), h(_.Affix, S(i(t), { container: i(o) }), v({ _: 2 }, [
      D(i(r), (l, c) => ({
        name: c,
        fn: b((u) => [
          y(e.$slots, c, A(x(u)))
        ])
      }))
    ]), 1040, ["container"]));
  }
}), j = {
  hover: !0,
  bordered: !0,
  tableLayout: "auto",
  showSortColumnBgColor: !0
};
function K(n) {
  return f(() => {
    const { pagination: t, data: r = [] } = n;
    let o;
    if (typeof t == "boolean") {
      if (!t)
        return;
      o = {
        defaultPageSize: 10
      };
    }
    return typeof t == "number" && t > 0 && (o = {
      defaultPageSize: t
    }), typeof t == "object" && t !== null && (o = t), {
      defaultCurrent: 1,
      total: r.length,
      ...o
    };
  });
}
function L(n) {
  let t = $(n.sort);
  const r = $([...n.data ?? []]);
  T(
    () => n.data,
    (a) => {
      r.value = [...a];
    }
  );
  const o = f(() => !n.columns && r.value.length > 0 ? R(r.value) : n.columns ?? []), {
    onSortChange: e,
    onDataChange: s,
    columns: l,
    multipleSort: c
  } = W({
    sort: t,
    tableData: r,
    columns: o
  }), u = f(() => ({
    ...j,
    ...n
  }));
  return {
    sort: t,
    tableData: r,
    onSortChange: e,
    onDataChange: s,
    columns: l,
    multipleSort: c,
    bindAttrs: u
  };
}
function R(n) {
  const t = n[0];
  return Object.keys(t).map((o) => ({
    colKey: o,
    title: o,
    sorter: !0
  }));
}
function O(n) {
  const t = n.colKey;
  return (r, o) => {
    const e = r[t], s = o[t];
    return e == null && s == null ? 0 : e == null ? 1 : s == null ? -1 : typeof e == "number" && typeof s == "number" ? e - s : e instanceof Date && s instanceof Date ? e.getTime() - s.getTime() : typeof e == "string" && typeof s == "string" ? e.localeCompare(s, void 0, { numeric: !0 }) : String(e).localeCompare(String(s), void 0, { numeric: !0 });
  };
}
function W(n) {
  const { tableData: t, sort: r, columns: o } = n, e = f(() => o.value.map((a) => a.sorter === !0 ? {
    ...a,
    sorter: O(a)
  } : a)), s = f(
    () => e.value?.some((a) => a.sorter)
  ), l = f(
    () => e.value.filter((a) => a.sorter).length > 1
  );
  return {
    onSortChange: (a, m) => {
      s.value && (r.value = a, t.value = [...m.currentDataSource ?? []]);
    },
    onDataChange: (a) => {
      t.value = a;
    },
    columns: e,
    multipleSort: l
  };
}
const q = /* @__PURE__ */ p({
  inheritAttrs: !1,
  __name: "Table",
  setup(n) {
    const t = d(), r = K(t), {
      sort: o,
      onSortChange: e,
      onDataChange: s,
      columns: l,
      multipleSort: c,
      tableData: u,
      bindAttrs: a
    } = L(t), m = C();
    return (w, J) => (g(), h(_.Table, S(i(a), {
      pagination: i(r),
      sort: i(o),
      data: i(u),
      columns: i(l),
      onSortChange: i(e),
      onDataChange: i(s),
      "multiple-sort": i(c)
    }), v({ _: 2 }, [
      D(i(m), (M, P) => ({
        name: P,
        fn: b((z) => [
          y(w.$slots, P, A(x(z)))
        ])
      }))
    ]), 1040, ["pagination", "sort", "data", "columns", "onSortChange", "onDataChange", "multiple-sort"]));
  }
});
function E(n) {
  const { affixProps: t = {} } = n;
  return {
    container: ".insta-main",
    ...t
  };
}
function F(n) {
  const { container: t = ".insta-main" } = n;
  return t;
}
const G = /* @__PURE__ */ p({
  inheritAttrs: !1,
  __name: "Anchor",
  setup(n) {
    const t = d(), r = C(), o = E(t), e = F(t);
    return (s, l) => (g(), h(_.Anchor, S(i(t), {
      container: i(e),
      "affix-props": i(o)
    }), v({ _: 2 }, [
      D(i(r), (c, u) => ({
        name: u,
        fn: b((a) => [
          y(s.$slots, u, A(x(a)))
        ])
      }))
    ]), 1040, ["container", "affix-props"]));
  }
}), H = /* @__PURE__ */ p({
  __name: "Icon",
  props: {
    name: {},
    size: {},
    color: {},
    prefix: {}
  },
  setup(n) {
    const t = n, r = f(() => {
      const [o, e] = t.name.split(":");
      return e ? t.name : `${t.prefix || "tdesign"}:${t.name}`;
    });
    return (o, e) => (g(), h(k("icon"), {
      class: "t-icon",
      icon: r.value,
      size: o.size,
      color: o.color
    }, null, 8, ["icon", "size", "color"]));
  }
});
function Q(n) {
  n.use(_), n.component("t-table", q), n.component("t-affix", B), n.component("t-anchor", G), n.component("t-icon", H);
}
export {
  Q as install
};
