import yfinance as yf
import math
import pandas as pd
from app import cache

def safe_get_forward_pe(ticker: str):
    t = yf.Ticker(_yahoo_symbol(ticker))
    val = None
    try:
        info = t.get_info()
        val = info.get("forwardPE", None)
    except Exception:
        pass
    if val is None:
        try:
            info = t.info
            val = info.get("forwardPE", None)
        except Exception:
            pass
    if val is None:
        try:
            fi = t.fast_info
            val = fi.get("forwardPE", fi.get("forward_pe", None))
        except Exception:
            pass
    try:
        if val is not None and not isinstance(val, (float, int)):
            val = float(val)
    except Exception:
        val = None
    if val is not None and (math.isnan(val) or math.isinf(val)):
        val = None
    return val

def safe_get_name(ticker: str):
    t = yf.Ticker(_yahoo_symbol(ticker))
    name = None
    try:
        info = t.get_info()
        name = info.get("shortName") or info.get("longName")
    except Exception:
        pass
    if not name:
        try:
            info = t.info
            name = info.get("shortName") or info.get("longName")
        except Exception:
            pass
    return name or ticker


def safe_get_market_cap(ticker: str):
    t = yf.Ticker(_yahoo_symbol(ticker))
    val = None
    try:
        fi = t.fast_info
        val = fi.get("market_cap", None)
    except Exception:
        pass
    if val is None:
        try:
            info = t.get_info()
            val = info.get("marketCap", None)
        except Exception:
            pass
    if val is None:
        try:
            info = t.info
            val = info.get("marketCap", None)
        except Exception:
            pass

    val = _to_float_safe(val)
    if val is not None and (math.isnan(val) or math.isinf(val) or val <= 0):
        val = None
    return val


def _to_float_safe(x):
    try:
        if x is None:
            return None
        return float(x)
    except Exception:
        return None

def _find_row_case_insensitive(df: pd.DataFrame, keys):
    if not isinstance(df, pd.DataFrame) or df.empty:
        return None
    norm = lambda s: "".join(str(s).lower().split()).replace("_", "")
    idx_map = {norm(i): i for i in df.index}
    for k in keys:
        nk = norm(k)
        if nk in idx_map:
            return df.loc[idx_map[nk]]
    return None

def safe_get_fcf_ttm(ticker: str):
    t = yf.Ticker(_yahoo_symbol(ticker))

    try:
        qcf = t.quarterly_cashflow
        if isinstance(qcf, pd.DataFrame) and not qcf.empty:
            row_fcf = _find_row_case_insensitive(
                qcf,
                ["Free Cash Flow", "FreeCashFlow", "Free cash flow"]
            )
            if row_fcf is not None:
                vals = [_to_float_safe(v) for v in row_fcf.values[:4]]
                vals = [v for v in vals if v is not None and not math.isnan(v)]
                if vals:
                    fcf_ttm = sum(vals)
                    if not math.isinf(fcf_ttm):
                        return fcf_ttm
            # ---- 2) Quarterly: считаем FCF = OCF - CapEx
            row_ocf = _find_row_case_insensitive(
                qcf,
                [
                    "Operating Cash Flow",
                    "Total Cash From Operating Activities",
                    "Net Cash Provided By Operating Activities",
                ]
            )
            row_capex = _find_row_case_insensitive(
                qcf,
                ["Capital Expenditures", "Capital Expenditure", "Capital Spending"]
            )
            if row_ocf is not None and row_capex is not None:
                ocf_vals = [_to_float_safe(v) for v in row_ocf.values[:4]]
                capex_vals = [_to_float_safe(v) for v in row_capex.values[:4]]
                fcf_vals = []
                for ocf, capex in zip(ocf_vals, capex_vals):
                    if ocf is not None and not math.isnan(ocf) and capex is not None and not math.isnan(capex):
                        fcf_vals.append(ocf - capex)  # CapEx часто отрицательный — формула универсальна
                if fcf_vals:
                    fcf_ttm = sum(fcf_vals)
                    if not math.isinf(fcf_ttm):
                        return fcf_ttm
    except Exception:
        pass

    try:
        acf = t.cashflow
        if isinstance(acf, pd.DataFrame) and not acf.empty:
            row_fcf_a = _find_row_case_insensitive(
                acf,
                ["Free Cash Flow", "FreeCashFlow", "Free cash flow"]
            )
            if row_fcf_a is not None:
                val = _to_float_safe(row_fcf_a.values[0] if len(row_fcf_a.values) > 0 else None)
                if val is not None and not math.isnan(val) and not math.isinf(val):
                    return val
            row_ocf_a = _find_row_case_insensitive(
                acf,
                [
                    "Operating Cash Flow",
                    "Total Cash From Operating Activities",
                    "Net Cash Provided By Operating Activities",
                ]
            )
            row_capex_a = _find_row_case_insensitive(
                acf,
                ["Capital Expenditures", "Capital Expenditure", "Capital Spending"]
            )
            if row_ocf_a is not None and row_capex_a is not None:
                ocf = _to_float_safe(row_ocf_a.values[0] if len(row_ocf_a.values) > 0 else None)
                capex = _to_float_safe(row_capex_a.values[0] if len(row_capex_a.values) > 0 else None)
                if ocf is not None and capex is not None and not math.isnan(ocf) and not math.isnan(capex):
                    fcf = ocf - capex
                    if not math.isinf(fcf):
                        return fcf
    except Exception:
        pass

    return None

def safe_get_cash_balance(ticker: str):
    t = yf.Ticker(_yahoo_symbol(ticker))
    for bs in (t.quarterly_balance_sheet, t.balance_sheet):
        try:
            if isinstance(bs, pd.DataFrame) and not bs.empty:
                row = _find_row_case_insensitive(
                    bs,
                    [
                        "Cash And Cash Equivalents",
                        "Cash",
                        "Cash And Cash Equivalents And Short Term Investments",
                    ]
                )
                if row is not None:
                    val = _to_float_safe(row.values[0] if len(row.values) > 0 else None)
                    if val is not None and not math.isnan(val) and not math.isinf(val):
                        return val
        except Exception:
            pass
    return None


def safe_get_total_debt(ticker: str):
    t = yf.Ticker(_yahoo_symbol(ticker))
    for bs in (t.quarterly_balance_sheet, t.balance_sheet):
        try:
            if isinstance(bs, pd.DataFrame) and not bs.empty:
                row_total = _find_row_case_insensitive(bs, ["Total Debt", "TotalDebt"])
                if row_total is not None:
                    val = _to_float_safe(row_total.values[0] if len(row_total.values) > 0 else None)
                    if val is not None and not math.isnan(val) and not math.isinf(val):
                        return val

                row_short = _find_row_case_insensitive(
                    bs,
                    ["Short Long Term Debt", "Short/Current Long Term Debt", "Current Debt"]
                )
                row_long = _find_row_case_insensitive(bs, ["Long Term Debt", "LongTermDebt"])

                short_v = _to_float_safe(row_short.values[0]) if row_short is not None and len(row_short.values) > 0 else None
                long_v  = _to_float_safe(row_long.values[0])  if row_long  is not None and len(row_long.values)  > 0 else None

                if (short_v is not None or long_v is not None):
                    total = (short_v or 0.0) + (long_v or 0.0)
                    if not math.isnan(total) and not math.isinf(total):
                        return total
        except Exception:
            pass
    return None


def safe_get_enterprise_value(ticker: str):
    t = yf.Ticker(_yahoo_symbol(ticker))
    mcap = safe_get_market_cap(ticker)
    if not mcap:
        return None

    candidates = []

    try:
        fi = t.fast_info
        candidates.append(_to_float_safe(fi.get("enterprise_value")))
    except Exception:
        pass

    for getter in (t.get_info, lambda: t.info):
        try:
            info = getter()
            candidates.append(_to_float_safe(info.get("enterpriseValue")))
        except Exception:
            pass

    debt = safe_get_total_debt(ticker) or 0.0
    cash = safe_get_cash_balance(ticker) or 0.0
    computed = mcap + debt - cash
    candidates.append(computed)

    def ok(x):
        return (x is not None) and (x > 0) and (not math.isinf(x)) and (not math.isnan(x))

    plausible = [x for x in candidates if ok(x) and (0.5*mcap <= x <= 3.0*mcap)]
    if plausible:
        return plausible[0]

    return computed if ok(computed) else (next((x for x in candidates if ok(x)), None))
def safe_get_ebit_ttm(ticker: str):
    t = yf.Ticker(_yahoo_symbol(ticker))
    try:
        qfin = t.quarterly_financials
        if isinstance(qfin, pd.DataFrame) and not qfin.empty:
            row = _find_row_case_insensitive(qfin, ["Ebit", "EBIT"])
            if row is not None:
                vals = [_to_float_safe(v) for v in row.values[:4]]
                vals = [v for v in vals if v is not None and not math.isnan(v)]
                if vals:
                    s = sum(vals)
                    if not math.isinf(s):
                        return s
    except Exception:
        pass
    try:
        fin = t.financials
        if isinstance(fin, pd.DataFrame) and not fin.empty:
            row = _find_row_case_insensitive(fin, ["Ebit", "EBIT"])
            if row is not None:
                val = _to_float_safe(row.values[0] if len(row.values) > 0 else None)
                if val is not None and not math.isnan(val) and not math.isinf(val):
                    return val
    except Exception:
        pass
    return None


def safe_get_ebitda_ttm(ticker: str):
    t = yf.Ticker(_yahoo_symbol(ticker))

    try:
        qfin = t.quarterly_financials
        if isinstance(qfin, pd.DataFrame) and not qfin.empty:
            row = _find_row_case_insensitive(qfin, ["Ebitda", "EBITDA"])
            if row is not None:
                vals = [_to_float_safe(v) for v in row.values[:4]]
                vals = [v for v in vals if v is not None and not math.isnan(v)]
                if vals:
                    s = sum(vals)
                    if not math.isinf(s):
                        return s
    except Exception:
        pass

    try:
        fin = t.financials
        if isinstance(fin, pd.DataFrame) and not fin.empty:
            row = _find_row_case_insensitive(fin, ["Ebitda", "EBITDA"])
            if row is not None:
                val = _to_float_safe(row.values[0] if len(row.values) > 0 else None)
                if val is not None and not math.isnan(val) and not math.isinf(val):
                    return val
    except Exception:
        pass

    return None

_US_SHARE_CLASS = {"BRK.B":"BRK-B", "BRK.A":"BRK-A", "BF.B":"BF-B", "HEI.A":"HEI-A", "LEN.B":"LEN-B"}
def _yahoo_symbol(tk: str) -> str:
    return _US_SHARE_CLASS.get(tk, tk)

def _cache_relpath(ticker: str) -> str:
    return f"yahoo/{ticker}.json"

def yahoo(tickers):
    rows = []
    for tk in tickers:
        rel = _cache_relpath(tk)
        data = cache.read_json(rel)

        if data is None:
            mcap = safe_get_market_cap(tk)
            fcf_ttm = safe_get_fcf_ttm(tk)

            p_to_fcf = None
            if mcap is not None and fcf_ttm is not None and fcf_ttm != 0:
                if fcf_ttm > 0:
                    p_to_fcf = mcap / fcf_ttm

            ev = safe_get_enterprise_value(tk)
            ebitda_ttm = safe_get_ebitda_ttm(tk)
            debt = safe_get_total_debt(tk)
            cash = safe_get_cash_balance(tk)

            ev_to_ebitda = None
            if ev is not None and ebitda_ttm is not None and ebitda_ttm > 0:
                ev_to_ebitda = ev / ebitda_ttm

            ebit_ttm = safe_get_ebit_ttm(tk)

            ev_to_ebit = None
            if ev is not None and ebit_ttm is not None and ebit_ttm > 0:
                ev_to_ebit = ev / ebit_ttm
            data = {
                "Ticker": tk,
                "Company": safe_get_name(tk),
                "Forward P/E": safe_get_forward_pe(tk),
                "P/FCF": p_to_fcf,
                "Market Cap": mcap,
                "FCF_TTM": fcf_ttm,
                "EV/EBITDA": ev_to_ebitda,
                "EV": ev,
                "EBITDA_TTM": ebitda_ttm,
                "EBIT_TTM": ebit_ttm,
                "EV/EBIT": ev_to_ebit,
                "Debt": debt,
                "Cash": cash,
            }

            cache.write_json(rel, data)

        rows.append(data)

    return rows