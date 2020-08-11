// fingerprint
// {
//   patient_age_years: integer
//   reason_for_visit: String
//   insurance: string
// }

// Rule Sets:
  // scenario_name = 'annual_exam_1'
  // reason = annual_exam
  // age between 20, 40

  // (num) => num >= 20 && num < 40
  // insurance = any
  // --> orders = ['folic acid', 'complete blood count']

  // scenario_name = 'annual_exam_2-medicare'
  // reason = annual_exam
  // age between 41+
  // insurance = medicare
  // --> orders = ['complete blood count', 'cancer screen']

  // scenario_name = 'annual_exam_2'
  // reason = annual_exam
  // age between 41+
  // insurance = !medicare
  // --> orders = ['complete blood count', 'a1c', 'cancer screen']

  // scenario_name = 'postop_hip'
  // reason = postop_hip
  // age = any
  // insurance = any
  // --> orders = ['xray, hip', 'stitch removal']

  // (fingerprint): orders[] =>

const ALL_RULES = [{
  name: 'annual_exam_1',
  reason: 'annual_exam',
  lowerAgeBound: 20,
  upperAgeBound: 40,
  insurance: [],
  orders: ['folic acid', 'complete blood count'],
  excludeInsurance: false,
}, {
  name: 'annual_exam_2',
  reason: 'annual_exam',
  lowerAgeBound: 41,
  insurance: ['medicare'],
  orders: ['folic acid', 'complete blood count'],
  excludeInsurance: false,
}];
const testFingerprints = [
  {
    patient_age_years: 31,
    insurance: 'aetna',
    reason_for_visit: 'annual_exam',
  },
  {
    patient_age_years: 300,
    insurance: 'aetna',
    reason_for_visit: 'annual_exam',
  },
]

class RuleSet {
  constructor({ name, insurance, reason, orders, lowerAgeBound, upperAgeBound, excludeInsurance }) {
    this.orders = orders;
    this.reason = reason;
    this.name = name;
    this.lowerAgeBound = lowerAgeBound || 0;
    this.upperAgeBound = upperAgeBound || Infinity;
    this.insurance = insurance;
    this.excludeInsurance = excludeInsurance;
  }

  validRule(fingerprint) {
    const { 
      patient_age_years,
      reason_for_visit,
      insurance,
    } = fingerprint;
    return (
      this.validAge(patient_age_years) &&
      this.validReason(reason_for_visit) &&
      this.validInsurance(insurance)
    );
  }

  validAge(age) {
    return age <= this.upperAgeBound && age >= this.lowerAgeBound;
  }

  validReason(reason) {
    return reason === this.reason;
  }

  validInsurance(insurance) {
    if (!this.insurance.length) return true;
    if (this.excludeInsurance) {
      return !this.insurance.includes(insurance)
    }
    return this.insurance.includes(insurance)
  }

  getAllOrders(fingerprint) {
    if (this.validRule(fingerprint)) return this.orders;
    return [];
  }
}
const seedRules = ALL_RULES.map((rule) => new RuleSet(rule));

const readFingerprint = (fingerprint) => {
  let resultingOrders = [];

  seedRules.forEach((rule) => {
    resultingOrders = [...resultingOrders, ...rule.getAllOrders(fingerprint)]
  });

  return resultingOrders;
}

testFingerprints.forEach(fingerprint => {
  console.log(readFingerprint(fingerprint));
})