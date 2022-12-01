exports.converter = function (base) {
  const chars = '0123456789abcdef';
  return (val) => {
    const converted = [];
    while (val > base) {
      converted.unshift(chars[val % base]);
      val = Math.floor(val / base);
    }
    converted.unshift(chars[val % base]);
    return converted.join('');
  };
};
